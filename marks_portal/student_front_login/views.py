from django.shortcuts import render

# Create your views here.

def login_page(request):
    if request.method=="POST":
        student_name=request.POST.get('Student_name')
        Password=request.POST.get('Password')

    return render(request,'index1.html')

#12.02 porjonto vedio dekhechi