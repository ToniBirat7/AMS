from django.shortcuts import render, redirect
from .models import Person
from .forms import ImageForm
# Create your views here.
def logged_In(request):
    if request.user.is_authenticated:
        # data1 = request.user.id
        # # print(data1)
        # data = Course_Teacher.objects.filter(user_id=data1)
        # # print(data[0].course.title)
        # for datas in data:
        #     # a = {'title' : datas.course.title , 'duration' :  datas.course.duration , 'shift' : datas.course.shift }
        #     print(datas.course.title, datas.course.duration, datas.course.shift)
        # # print(a)
        return render(request,'attendance/course_list.html')
    else:
        return redirect('login')
    

def Profile(request):
    user_id = request.user.id
    print(user_id)
    data = Person.objects.get(user_id=user_id)
    print(data.user.date_joined)  
    form = ImageForm()
    return render(request, 'attendance/profile.html', {'profile' : data , 'form' : form} )

'''{% extends "core/base.html" %}
{% block body %}
{% for datas in data %}
<p>{{datas.address}}</p>
{% endfor %}
<p>{{data.user}}</p>

{% endblock body %}'''

def EditProfile(request):
    return render(request, 'attendance/edit-profile.html')