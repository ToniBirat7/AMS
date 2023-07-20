from django.contrib import admin
# Register your models here.
from .models import Course , Student, Person, Class

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['id','title','duration','shift','person']

@admin.register(Student)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

@admin.register(Person)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['id','user','primary_number','secondary_number','sex','my_image','address','DOB','is_student']

@admin.register(Class)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['id','course','student']


