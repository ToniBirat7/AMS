from django.shortcuts import render, redirect
from datetime import date , timedelta, datetime
import calendar
from .models import Date, Attendance
from Attendance.models import Student
from .models import Attendance, Date
from django.contrib import messages

# to display today's date in calendar
todays_date = date.today()
year = todays_date.year
day = todays_date.day

# calender iterator object for calendar
cal = calendar.Calendar()
cal.setfirstweekday(6)
month_name = calendar.month_name[todays_date.month]

# to display calendar 
def Display_Calendar(request):
    cal_data = cal.itermonthdays(year,todays_date.month)
    # for day in cal_data:
    #     print(day)
    return render(request,'attendance/calendar.html', {'month': month_name, 'today_date':todays_date, 'calendar': cal_data})

# after choosing date from calendar 
# another calendar obj because iterator once consumed gets exhausted
# student's status of 7 days prior today 
# after choosing date create date object in Date Model
# for form submission take date id for today's date and
# student status using student id from POST data 
# saving the data in Attendance Model by creating object 
def ChooseDate(request,date):
    student_list = Student.objects.all().order_by('name') # student data for student list 
    new_date = datetime.strptime(date,"%Y-%m-%d").date()
    print(type(date))
    print(type(new_date))
    if request.method == 'POST':
        Date.objects.create(today_date = new_date)
        date_info = Date.objects.get(today_date = new_date)
        print('***************')
        print(type(date_info.today_date))
        print('Date Info')
        print(request.POST)
        for student in student_list:
            status_value = request.POST[str(student.id)]
            print('Student Info')
            print(student.id,status_value)
            Attendance.objects.create(date_id = date_info.id, student_id = student.id, status = status_value)
        return render(request,'calendar/student_list.html',{'data': student_list,'month': month_name,'today_date': todays_date})   
    else:
        start_week = todays_date - timedelta(days=7)
        end_week = start_week + timedelta(days=6)
        print('***************')
        print(start_week, end_week)
        past_date = Date.objects.filter(today_date__range=[start_week, end_week])
        for d in past_date:
            print('pppp*********')
            print(d.today_date)
            print(d.today_date.day)
        return render(request,'calendar/student_list.html', {'data': student_list,'month': month_name,'today_date': todays_date,'past_date': past_date})



    
