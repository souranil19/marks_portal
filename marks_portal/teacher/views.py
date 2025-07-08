from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Teacher, ClassAccess
from student_front_login.models import Student, StudentTermSummary

# ----------------------------
# LOGIN VIEW
# ----------------------------
def teacher_login_page(request):
    if request.session.get('teacher_is_authenticated'):
        return redirect('teacher_dashboard')

    if request.method == 'POST':
        teacher = request.POST.get('teacher')
        password = request.POST.get('password')
        selection_option = request.POST.get('selection_option')

        if teacher and password and selection_option:
            try:
                teacher_obj = Teacher.objects.get(teacher=teacher, password=password)

                # Store session
                request.session['teacher_password'] = teacher_obj.password
                request.session['teacher'] = teacher_obj.teacher
                request.session['teacher_is_authenticated'] = True
                request.session.set_expiry(1800)  # 30 min

                # Redirect based on selection
                if selection_option == 'dashboard':  # Teacher Dashboard
                    return redirect('teacher_dashboard')
                elif selection_option == 'profile':  # Teacher Details Update
                    return redirect('teacher_details_update')
                else:
                    return redirect('teacher_dashboard')  # Default fallback
                    
            except Teacher.DoesNotExist:
                messages.error(request, 'Invalid teacher name or password.')
        else:
            messages.error(request, 'Please fill in all fields')

    return render(request, 'teacher_login.html',)


# ----------------------------
# LOGOUT VIEW
# ----------------------------
def teacher_logout_view(request):
    request.session.flush()
    messages.success(request, 'Logged out successfully.')
    return redirect('teacher_login_page')


# ----------------------------
# DECORATOR TO PROTECT VIEWS
# ----------------------------
def teacher_login_required(view_func):
    def wrapper(request, *args, **kwargs):
        if not request.session.get('teacher_is_authenticated'):
            messages.error(request, 'Login required to access this page.')
            return redirect('teacher_login_page')
        return view_func(request, *args, **kwargs)
    return wrapper


# ----------------------------
# PROTECTED VIEW: TEACHER DASHBOARD
# ----------------------------

@teacher_login_required
def teacher_dashboard(request):
    teacher_password = request.session.get('teacher_password')
    teacher = request.session.get('teacher')
    teacher_obj = Teacher.objects.get(teacher=teacher, password=teacher_password)

    return render(request, 'teacher_dashboard.html', {
        'teacher': teacher_obj,
        'teacher_name': teacher_obj.teacher
    })



# ----------------------------
# PROTECTED VIEW: TEACHER DETAILS UPDATE
# ----------------------------




@teacher_login_required
def teacher_details_update(request):
    teacher_sesson = request.session.get('teacher')
    teacher = Teacher.objects.get(teacher=teacher_sesson)
    
    if request.method == 'POST':
        # Get form data
        mobile = request.POST.get('mobile')
        password = request.POST.get('password')
        img = request.FILES.get('img')
        pdf_document = request.FILES.get('pdf_document')
        
        try:
            # Update teacher fields
            if mobile:
                teacher.mobile = int(mobile) if mobile.isdigit() else None
            if password:
                teacher.password = password
            if img:
                teacher.img = img
            if pdf_document:
                teacher.pdf_document = pdf_document
            
            # Save the updated teacher
            teacher.save()
            messages.success(request, 'Details updated successfully!')
            return redirect('teacher_details_update')
            
        except ValueError as e:
            messages.error(request, 'Invalid data provided. Please check your inputs.')
        except Exception as e:
            messages.error(request, 'An error occurred while updating details. Please try again.')
    
    return render(request, 'teacher_details_update.html', {
        'teacher': teacher,
        'teacher_name': teacher.teacher
    })


# ----------------------------
# PROTECTED VIEW: CLASS ACCESS
# ----------------------------

@teacher_login_required
def class_access_view(request, class_number):
    try:
        class_obj = ClassAccess.objects.get(class_number=class_number)
    except ClassAccess.DoesNotExist:
        messages.error(request, f'Class {class_number} not found or not configured.')
        return redirect('teacher_dashboard')
    
    if request.method == 'POST':
        entered_password = request.POST.get('class_password')
        
        if entered_password == class_obj.class_password:
            # Store class access in session
            request.session[f'class_{class_number}_access'] = True
            request.session.set_expiry(1800)  # 30 min
            return redirect('marks_entry', class_number=class_number)
        else:
            messages.error(request, 'Incorrect class password. Please try again.')
    
    return render(request, 'class_access.html', {
        'class_obj': class_obj,
        'class_number': class_number
    })


# ----------------------------
# PROTECTED VIEW: MARKS ENTRY
# ----------------------------

@teacher_login_required
def marks_entry_view(request, class_number):
    # Check if teacher has access to this class
    if not request.session.get(f'class_{class_number}_access'):
        messages.error(request, 'Please enter the class password first.')
        return redirect('class_access', class_number=class_number)
    
    # Get students in this class
    students = Student.objects.filter(std=class_number)
    
    if request.method == 'POST':
        student_id = request.POST.get('student_id')
        subject = request.POST.get('subject')
        term = request.POST.get('term')
        mark_type = request.POST.get('mark_type')  # theory or practical
        marks = request.POST.get('marks')
        
        try:
            student = Student.objects.get(id=student_id)
            
            # Get or create StudentTermSummary for this student
            term_summary, created = StudentTermSummary.objects.get_or_create(student=student)
            
            # Create the field name dynamically
            field_name = f"{subject}_{term}_{mark_type}"
            
            # Update the marks
            if hasattr(term_summary, field_name):
                setattr(term_summary, field_name, int(marks))
                term_summary.save()
                messages.success(request, f'Marks updated successfully for {student.student_name}!')
            else:
                messages.error(request, 'Invalid subject or term selection.')
                
        except (Student.DoesNotExist, ValueError) as e:
            messages.error(request, 'Error updating marks. Please check your inputs.')
    
    # Get existing marks for display
    students_with_marks = []
    for student in students:
        term_summary, created = StudentTermSummary.objects.get_or_create(student=student)
        students_with_marks.append({
            'student': student,
            'term_summary': term_summary
        })
    
    subjects = ['bengali', 'english', 'mathematics', 'physical_science', 'life_science', 'history', 'geography']
    terms = ['first', 'second', 'third']
    mark_types = ['theory', 'practical']
    
    return render(request, 'marks_entry.html', {
        'class_number': class_number,
        'students_with_marks': students_with_marks,
        'subjects': subjects,
        'terms': terms,
        'mark_types': mark_types
    })
