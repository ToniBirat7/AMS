from django.contrib import admin
# Register your models here.
from .models import  Course_Teacher , Course , Student, Attendance

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['id','title','duration','shift','starting_date']

@admin.register(Course_Teacher)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'course']


@admin.register(Student)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['id', 'name','roll_no', 'course_enrolled']

@admin.register(Attendance)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['id', 'date','student', 'status']



