from django.shortcuts import render, redirect
import calendar
# Create your views here.
def Display_Calendar(request):
    cal = calendar.HTMLCalendar()
    b = cal.formatmonth(2023,2)
    return render(request,'attendance/calendar.html', {'cal': b})

    
