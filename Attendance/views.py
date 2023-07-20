from django.shortcuts import render, redirect
from .models import Person,Course
from .forms import ImageForm

# Create your views here.
def logged_In(request):
    user_id = request.user.id
    teacher_detail = Person.objects.get(user_id = user_id)
    course_detail = Course.objects.filter(person_id = teacher_detail.id)
    print(course_detail)
    for d in course_detail:
        print(d.title)
    if request.user.is_authenticated:
        if request.method == 'GET':
            return render(request,'attendance/course_list.html', {'course_detail' : course_detail})
        else:
            status = request.POST['status']   
        print(status)
    else:
        return redirect('login')
 
def Profile(request):
    user_id = request.user.id
    teacher_detail = Person.objects.get(user_id=user_id)
    course_detail = Course.objects.filter(person_id = teacher_detail.id)
    print(teacher_detail.user.first_name)
    if teacher_detail is not None:
        if request.method == 'GET':
            form = ImageForm()
        else:
            form = ImageForm(request.POST, request.FILES)
            if form.is_valid():
                img = form.cleaned_data['image']
                teacher_detail.my_image = img
                teacher_detail.save()
    else:
        print('Invalid User')
    return render(request, 'attendance/profile.html', {'profile' : teacher_detail , 'form' : form,'course_detail': course_detail} )

def ImageDelete(request):
    user_id = request.user.id
    data = Person.objects.get(user_id=user_id)
    data.my_image.delete()
    data.my_image = 'NA'
    data.save()
    return redirect('profile')

def EditProfile(request):
    user_id = request.user.id
    if request.method == 'GET':
        data = Person.objects.get(user_id=user_id)
        return render(request, 'attendance/edit-profile.html',{'datas' : data})
    else:
        data = Person.objects.get(user_id=user_id)
        print(data.id)
        print(request.POST)
        data.primary_number = request.POST['primary_number']
        data.address = request.POST['address']
        data.secondary_number = request.POST['secondary_number']
        data.save()
    return redirect('profile')








