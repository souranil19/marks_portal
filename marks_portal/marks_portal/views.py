from django.shortcuts import render, redirect
from django.http import HttpResponse

def school_landing(request):
    return render(request,'landing1.html')

def about(request):
    return render(request, 'about.html')


def morning_school_landing(request):
    return render(request,'morning_school_landing1.html')

def day_school_landing(request):
    return render(request,'day_school_landing1.html')

def vocational_landing(request):
    return render(request,'vocational_landing1.html')


def notice(request):
    return render(request,'notice.html')


def contact(request):
    return render(request,'contact.html')


def gallery(request):
    return render(request,'gallery.html')