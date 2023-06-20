from django.shortcuts import render, redirect
from .forms import LogForm, ForgotPswd
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.forms import SetPasswordForm
# Create your views here.

def Login(request):
    if request.method == "POST":
        print(request.POST)
        logform = LogForm(data=request.POST)
        print(logform.is_valid())
        if logform.is_valid():
            print('*********')
            un = logform.cleaned_data['username']
            pw = logform.cleaned_data['password']
            print(un,pw)
            user = authenticate(username=un,password=pw)
            if user is not None:
                login(request,user)
                messages.success(request, "You've successfully logged in!!")
                return redirect('logged_in')   
        else: 
            print('Not Valid')
            messages.warning(request,"These credentials do not match our records!")
    else:
        logform = LogForm()
    return render(request, 'auth/login.html', {'form': logform})

def Logout(request):
    log_user = request.user.id
    print(log_user)
    logout(request)
    return redirect('login')

def Forgotpswd(request):
    if request.method == 'POST':
        form = ForgotPswd(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            print('Not Valid')
            return render(request,'auth/forgotpswd.html', {'form':form})
    else:
        form = ForgotPswd(user=request.user)
    return render(request,'auth/forgotpswd.html', {'form':form})
     


