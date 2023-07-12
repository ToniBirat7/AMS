from django.contrib import admin
from .models import Date, Attendance
# Register your models here.

@admin.register(Date)
class AdminRegister(admin.ModelAdmin):
    list_display = ['today_date']

@admin.register(Attendance)
class AdminRegister(admin.ModelAdmin):
    list_display = ['date','student','status']