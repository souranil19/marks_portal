from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Teacher

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
