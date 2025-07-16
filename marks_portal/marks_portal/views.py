from django.shortcuts import render
from django.http import HttpResponse

def school_landing(request):
    return render(request,'landing1.html')