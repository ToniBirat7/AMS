from django.contrib import admin
from .models import Attendance
# Register your models here.



@admin.register(Attendance)
class AdminRegister(admin.ModelAdmin):
    list_display = ['today_date','student','status','course']