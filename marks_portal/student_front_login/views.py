from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Student, StudentTermSummary

# ----------------------------
# LOGIN VIEW
# ----------------------------
def login_page(request):
    if request.session.get('is_authenticated'):
        return redirect('mark_sheet')

    if request.method == 'POST':
        student_name = request.POST.get('student_name')
        password = request.POST.get('password')
        selection_option = request.POST.get('selection_option')

        if student_name and password and selection_option:
            try:
                student = Student.objects.get(student_name=student_name, password=password)

                # Store session
                request.session['student_id'] = student.id
                request.session['student_name'] = student.student_name
                request.session['is_authenticated'] = True
                request.session.set_expiry(1800)  # 30 min

                # Redirect based on selection
                if selection_option == 'notices':  # Student Marks
                    return redirect('mark_sheet')
                elif selection_option == 'profile':  # Student Details Update
                    return redirect('details_update')
                else:
                    return redirect('mark_sheet')  # Default fallback
                    
            except Student.DoesNotExist:
                messages.error(request, 'Invalid student name or password.')
        else:
            messages.error(request, 'Please fill in all fields')

    return render(request, 'index1.html',)


# ----------------------------
# LOGOUT VIEW
# ----------------------------
def logout_view(request):
    request.session.flush()
    messages.success(request, 'Logged out successfully.')
    return redirect('login_page')


# ----------------------------
# DECORATOR TO PROTECT VIEWS
# ----------------------------
def login_required(view_func):
    def wrapper(request, *args, **kwargs):
        if not request.session.get('is_authenticated'):
            messages.error(request, 'Login required to access this page.')
            return redirect('login_page')
        return view_func(request, *args, **kwargs)
    return wrapper


# ----------------------------
# PROTECTED VIEW: MARK SHEET
# ----------------------------

@login_required
def mark_sheet(request):
    student_id = request.session.get('student_id')
    student = Student.objects.get(id=student_id)
    
    # Get or create StudentTermSummary for this student
    term_summary, created = StudentTermSummary.objects.get_or_create(student=student)
    
    # Simple subject list - let JavaScript handle calculations
    subjects = [
        ('BENGALI', 'bengali'),
        ('ENGLISH', 'english'), 
        ('MATHEMATICS', 'mathematics'),
        ('PHYSICAL SCIENCE', 'physical_science'),
        ('LIFE SCIENCE', 'life_science'),
        ('HISTORY', 'history'),
        ('GEOGRAPHY', 'geography')
    ]
    
    # Prepare simple subjects data without calculations
    subjects_data = []
    for subject_name, subject_code in subjects:
        subjects_data.append({
            'name': subject_name,
            'code': subject_code,
            'first_theory': getattr(term_summary, f'{subject_code}_first_theory') or 0,
            'first_practical': getattr(term_summary, f'{subject_code}_first_practical') or 0,
            'second_theory': getattr(term_summary, f'{subject_code}_second_theory') or 0,
            'second_practical': getattr(term_summary, f'{subject_code}_second_practical') or 0,
            'third_theory': getattr(term_summary, f'{subject_code}_third_theory') or 0,
            'third_practical': getattr(term_summary, f'{subject_code}_third_practical') or 0,
        })

    return render(request, 'marks.html', {
        'student': student,
        'student_name': student.student_name,
        'term_summary': term_summary,
        'subjects_data': subjects_data
    })




# ----------------------------
# PROTECTED VIEW: STUDENT DETAILS UPDATE
# ----------------------------

@login_required
def details_update(request):
    student_id = request.session.get('student_id')
    student = Student.objects.get(id=student_id)
    
    if request.method == 'POST':
        # Get form data
        student_code = request.POST.get('student')
        mobile = request.POST.get('mobile')
        std = request.POST.get('std')
        father = request.POST.get('father')
        dob = request.POST.get('dob')
        password = request.POST.get('password')
        address = request.POST.get('address')
        img = request.FILES.get('img')
        
        try:
            # Update student fields (excluding student_name as it cannot be updated)
            if student_code:
                student.student = student_code
            if mobile:
                student.mobile = int(mobile) if mobile.isdigit() else None
            if std:
                student.std = int(std) if std.isdigit() else None
            if father:
                student.father = father
            if dob:
                student.dob = dob
            if password:
                student.password = password
            if address:
                student.address = address
            if img:
                student.img = img
            
            # Save the updated student
            student.save()
            messages.success(request, 'Details updated successfully!')
            return redirect('details_update')
            
        except ValueError as e:
            messages.error(request, 'Invalid data provided. Please check your inputs.')
        except Exception as e:
            messages.error(request, 'An error occurred while updating details. Please try again.')
    
    return render(request, 'details_update.html', {
        'student': student,
        'student_name': student.student_name
    })