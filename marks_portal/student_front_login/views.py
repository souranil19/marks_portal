from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password
from django.utils.crypto import get_random_string
from .models import Student
import hashlib
import secrets

def login_page(request):
    # Redirect to marks if already authenticated
    if is_authenticated(request):
        return redirect('mark_sheet')
        
    if request.method == "POST":
        student_name = request.POST.get('student_name')
        password = request.POST.get('password')
        print(f"POST data received - student_name: {student_name}, password: {password}")
        
        if student_name and password:  # Check if both values are not None/empty
            try:
                student = Student.objects.get(student_name=student_name, password=password)
                print("Student found, setting secure session and redirecting...")
                
                # Create a secure session token
                session_token = secrets.token_urlsafe(32)
                session_hash = hashlib.sha256(f"{student.id}{student_name}{session_token}".encode()).hexdigest()
                
                # Store secure session data
                request.session['student_id'] = student.id
                request.session['student_name'] = student_name
                request.session['session_token'] = session_token
                request.session['session_hash'] = session_hash
                request.session['is_authenticated'] = True
                
                # Set session expiry (30 minutes)
                request.session.set_expiry(1800)
                
                return redirect('mark_sheet')
            except Student.DoesNotExist:
                print("Student not found in database")
                messages.error(request, "Invalid ID or Username. Please try again.")
        else:
            print("Missing student_name or password")
            messages.error(request, "Please fill in both fields.")
    
    return render(request, 'index1.html')



def require_authentication(view_func):
    """
    Decorator to require authentication for views
    """
    def wrapper(request, *args, **kwargs):
        if not is_authenticated(request):
            request.session.flush()
            messages.error(request, "Please login to access this page.")
            return redirect('login_page')
        return view_func(request, *args, **kwargs)
    return wrapper


def is_authenticated(request):
    """
    Verify if the user is properly authenticated by checking:
    1. Required session variables exist
    2. Session hash is valid
    3. Student exists in database
    4. Session hasn't expired
    """
    required_fields = ['student_id', 'student_name', 'session_token', 'session_hash', 'is_authenticated']
    
    # Check if all required session fields exist
    if not all(field in request.session for field in required_fields):
        return False
    
    # Check if is_authenticated flag is True
    if not request.session.get('is_authenticated'):
        return False
    
    try:
        # Verify student exists in database
        student_id = request.session.get('student_id')
        student_name = request.session.get('student_name')
        student = Student.objects.get(id=student_id, student_name=student_name)
        
        # Verify session hash
        session_token = request.session.get('session_token')
        expected_hash = hashlib.sha256(f"{student.id}{student_name}{session_token}".encode()).hexdigest()
        stored_hash = request.session.get('session_hash')
        
        if expected_hash != stored_hash:
            return False
            
        return True
        
    except Student.DoesNotExist:
        return False
    except Exception as e:
        print(f"Authentication error: {e}")
        return False


@require_authentication
def mark_sheet(request):
    print("mark_sheet view called")
    print(f"Session data: {dict(request.session.items())}")
    
    print("Authentication successful, rendering marks.html")
    # Get student data for the template
    student_id = request.session.get('student_id')
    student = Student.objects.get(id=student_id)
    
    context = {
        'student': student,
        'student_name': student.student_name
    }
    
    return render(request, 'marks.html', context)



def logout_view(request):
    """
    Securely logout the user by clearing all session data
    """
    print("Logging out user, clearing session")
    request.session.flush()  # Completely clear the session
    messages.success(request, "You have been logged out successfully.")
    return redirect('login_page')



















#12.02 porjonto vedio dekhechi
"""

if UserID.objects.filter(unique_id=entered_id, username=entered_name).exists():
            request.session['unique_id'] = entered_id
            request.session['username'] = entered_name
            return redirect('main')
        else:
            messages.error(request, "Invalid ID or Username. Please try again.")


"""