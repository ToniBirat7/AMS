from django.shortcuts import render, redirect
from .forms import LogForm
from .models import Course_Teacher, Course
from django.contrib.auth.models import User


# Create your views here.

def Login(request):
    logForm = LogForm()
    print(logForm) 
    if request.method == "GET":
        return render(request, 'auth/login.html', { 'form': logForm})
    else: 
        logform = LogForm(request.POST)
        if logform.is_valid():
            clean_form = logform.cleaned_data
            un = clean_form.username
            pw = clean_form.password
        
def Login_Complete(request):
    logForm = LogForm()
    print(logForm) 
    if request.method == "GET":
        return render(request, 'auth/reg.html', { 'form': logForm})
    else: 
        logform = LogForm(request.POST)
        if logform.is_valid():
            clean_form = logform.cleaned_data
            un = clean_form.username
            pw = clean_form.password
            return render(request, 'auth/reg.html', {'form' : logform })


