from django.shortcuts import render, redirect
from .forms import LogForm, ForgotPswd
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.forms import SetPasswordForm
from django.contrib.auth.models import User
from .forms import PersonForm
from Attendance.models import Person, Course, Student, Class
from django.contrib.auth.decorators import login_required
# Create your views here.

def Login(request):
    if request.method == "POST":
        # print(request.POST)
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
            if user.is_superuser:
                return redirect('admin-page')
                # return redirect('logged_in') 
            else:
                return redirect('logged_in')
        else: 
            print('Not Valid')
            # messages.warning(request,"These credentials do not match our records!")
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


def UserRegistration(request):
    print(request.POST)
    if request.method == "POST":
        fn = request.POST.get("first_name")
        ln = request.POST.get("last_name")
        un = request.POST.get("username")
        em = request.POST.get("email")
        print(em)
        pw1 = request.POST.get("pswd1")
        pw2 = request.POST.get("pswd2")
        if pw1 == pw2:
            if User.objects.filter(username=un).exists():
                messages.info(request,f"The User With {un} already exists")
                print("User Exists")
                return render(request,'auth/registration.html')
            else:
                user = User.objects.create_user(username=un,first_name=fn,last_name=ln,password=pw1,email=em)
                user.save()
                messages.info(request,"User Has Been Sucessfully Registered")
            print("Matches")
        else:
            messages.info(request,"The passwords didn't matched")
            return render(request,'auth/registration.html')
    else: 
        pass
    return render(request,'auth/registration.html')

def PersonRegistration(request):
    # print(request.POST,request.FILES)
    user_list = User.objects.prefetch_related().all()
    # print(user_list) 
    if request.method == "POST":
        print('*************8')
        print(request.FILES)
        print(request.POST)
        data = request.FILES['my_image']
        print(data)
        Person.objects.create(user_id=request.POST['teacher'],address=request.POST['address'],DOB=request.POST['DOB'],primary_number=request.POST['primary_number'],secondary_number=request.POST['secondary_number'],my_image=request.FILES['my_image'],sex=request.POST['sex'])
        messages.info(request,'Teacher Detail Added Successfully!')
    else:
        pass
    return render(request,'auth/PersonRegistration.html',{'teacher':user_list})
@login_required
def AdminPage(request):
    person_list = Person.objects.prefetch_related().all()
    stu_list = Student.objects.all()
    for s in stu_list:
        print(s.name)
    return render(request,'auth/admin.html',{'persons':person_list,'students':stu_list})

def AddCourse(request):
    user_list = Person.objects.prefetch_related().all()
    if request.method == "POST":
        print(request.POST)
        Course.objects.create(person_id=request.POST['teacher'],title=request.POST['title'],shift=request.POST['shift'],duration=request.POST['duration'])
        messages.info(request,'Course Added Successfully!')
    else:
        pass
    return render(request,'auth/addcourse.html',{'teacher':user_list})

def AddStudent(request):
    if request.method == "POST":
        print(request.POST['name'])
        Student.objects.create(name=request.POST['name'],address=request.POST['address'],phone_number=request.POST['phone_number'],age=request.POST['age'])
        messages.info(request,'Student Added Successfully!')
    else:
        pass
    return render(request,'auth/addstudent.html')

def AddClass(request):
    course_list = Course.objects.prefetch_related().all()
    stu_list = Student.objects.all()
    if request.method == 'POST':
        print(request.POST)
        selected_students = [int(id) for id in request.POST.getlist('student')]
        print("Student",selected_students)
        if selected_students:
            for student in selected_students:
                Class.objects.create(course_id=request.POST['course'],student_id=student)
                messages.info(request,'Students Added to Class Successfully!')
        else:
            print("No Data")
    else:
        pass
    return render(request,'auth/addclass.html',{'students': stu_list,'courses':course_list})

     


