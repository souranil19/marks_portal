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
        teacher_name = request.POST.get('teacher_name')
        password = request.POST.get('password')
        selection_option = request.POST.get('selection_option')

        if teacher_name and password and selection_option:
            try:
                teacher = Teacher.objects.get(teacher_name=teacher_name, password=password)

                # Store session
                request.session['teacher_id'] = teacher.id
                request.session['teacher_name'] = teacher.teacher_name
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

def teacher_dashboard(request):
    teacher_id = request.session.get('teacher_id')
    teacher = Teacher.objects.get(id=teacher_id)

    return render(request, 'teacher_dashboard.html', {
        'teacher': teacher,
        'teacher_name': teacher.teacher_name
    })


@teacher_login_required
def teacher_details_update(request):
    teacher_id = request.session.get('teacher_id')
    teacher = Teacher.objects.get(id=teacher_id)
    
    if request.method == 'POST':
        # Get form data
        teacher_code = request.POST.get('teacher')
        mobile = request.POST.get('mobile')
        subject = request.POST.get('subject')
        qualification = request.POST.get('qualification')
        dob = request.POST.get('dob')
        password = request.POST.get('password')
        address = request.POST.get('address')
        img = request.FILES.get('img')
        
        try:
            # Update teacher fields (excluding teacher_name as it cannot be updated)
            if teacher_code:
                teacher.teacher = teacher_code
            if mobile:
                teacher.mobile = int(mobile) if mobile.isdigit() else None
            if subject:
                teacher.subject = subject
            if qualification:
                teacher.qualification = qualification
            if dob:
                teacher.dob = dob
            if password:
                teacher.password = password
            if address:
                teacher.address = address
            if img:
                teacher.img = img
            
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
        'teacher_name': teacher.teacher_name
    })
