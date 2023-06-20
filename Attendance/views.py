from django.shortcuts import render, redirect
from auth_app.models import Course_Teacher
# Create your views here.
def logged_In(request):
    if request.user.is_authenticated:
        return render(request,'attendance/course_list.html')
    else:
        return redirect('login')