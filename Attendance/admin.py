from django.contrib import admin
# Register your models here.
from .models import Course , Student, Person 

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['id','title','duration','shift','starting_date']


@admin.register(Student)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['id', 'name','roll_no', 'course_enrolled']

@admin.register(Person)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['id', 'user','course', 'primary_number','secondary_number','sex','my_image','address','DOB']




