from django.shortcuts import render
from django.http import HttpResponse

def school_landing(request):
    return render(request,'landing1.html')

def morning_school_landing(request):
    return render(request,'morning_school_landing1.html')

def day_school_landing(request):
    return render(request,'day_school_landing1.html')

def vocational_landing(request):
    return render(request,'vocational_landing1.html')