# Create your views here.
from django.shortcuts import render

def home(request):
    return render(request,'main/home.html')

def contact(request):
    return render(request,'main/contact.html')

def projects(request):
    return render(request,'main/projects.html')

def resume(request):
    return render(request, 'main/resume.html')

def help(request):
    return render(request, 'main/help.html')

def help2(request):
    return render(request, 'main/help2.html')