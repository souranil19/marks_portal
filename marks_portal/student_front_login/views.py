from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.

def login_page(request):
    if request.method=="POST":
        student_name=request.POST.get('Student_name')
        Password=request.POST.get('Password')

        user=authenticate(student_name=student_name,Password=Password)

        if user is None:
            messages.error(request,'Invalid student name or password')
            return render(request,'index1.html')
        
        else:
            login(request,user)
            return redirect('marksheet/')


    #return render(request,'index1.html')



def mark_sheet(request):
    return render(request,'marks.html')
#12.02 porjonto vedio dekhechi


""" FIRST LOGIC -----------------

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import UserID

def login_view(request):
    if request.method == 'POST':
        entered_id = request.POST.get('unique_id', '').strip()
        entered_name = request.POST.get('username', '').strip()

        # Check if both unique_id and username match
        if UserID.objects.filter(unique_id=entered_id, username=entered_name).exists():
            request.session['unique_id'] = entered_id
            request.session['username'] = entered_name
            return redirect('main')
        else:
            messages.error(request, "Invalid ID or Username. Please try again.")
    
    return render(request, 'login.html')



    
SECOND LOGIC------------------------
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import UserID

def login_view(request):
    if request.method == 'POST':
        entered_id = request.POST.get('unique_id', '').strip()
        if UserID.objects.filter(unique_id=entered_id).exists():
            request.session['unique_id'] = entered_id
            return redirect('main')  # Redirect to the main page
        else:
            messages.error(request, "Invalid ID. Please try again.")
    
    return render(request, 'login.html')

    
def main_view(request):
    if 'unique_id' not in request.session:
        return redirect('login')
    return render(request, 'main.html')



"""