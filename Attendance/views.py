from django.shortcuts import render, redirect
from .models import Person
from .forms import ImageForm

# Create your views here.
def logged_In(request):
    user_id = request.user.id
    if request.user.is_authenticated:
        if request.method == 'GET':
            course = Person.objects.get(user_id = user_id)
            return render(request,'attendance/course_list.html', {'course' : course})
        else:
            status = request.POST['status']   
        print(status)
    else:
        return redirect('login')
    

def Profile(request):
    user_id = request.user.id
    data = Person.objects.get(user_id=user_id)
    print(data.user.first_name)
    if data is not None:
        if request.method == 'GET':
            form = ImageForm()
        else:
            form = ImageForm(request.POST, request.FILES)
            if form.is_valid():
                img = form.cleaned_data['image']
                data.my_image = img
                data.save()
    else:
        print('Invalid User')
    return render(request, 'attendance/profile.html', {'profile' : data , 'form' : form} )

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
        # data.DOB = request.POST['DOB']
        data.primary_number = request.POST['primary_number']
        data.address = request.POST['address']
        data.secondary_number = request.POST['secondary_number']
        data.save()
    return redirect('profile')








