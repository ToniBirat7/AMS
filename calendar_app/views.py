from django.shortcuts import render, redirect
from datetime import date, timedelta, datetime
import calendar
from .models import  Attendance
from Attendance.models import Student,Class
from django.contrib import messages
import pandas as pd, openpyxl 
from django.http import HttpResponse
from django.utils.encoding import escape_uri_path

# to display today's date in calendar
todays_date = date.today()
year = todays_date.year
day = todays_date.day

# calender iterator object for calendar
cal = calendar.Calendar()
cal.setfirstweekday(6)
month_name = calendar.month_name[todays_date.month]

# to display calendar 
def Display_Calendar(request,course_id):
    global course_id_global
    course_id_global = course_id
    cal_data = cal.itermonthdays(year,todays_date.month)
    print('*************')
    global student_list
    student_list = Class.objects.filter(course_id = course_id)
    for s in student_list:
        print(s.student.name) 
    return render(request,'attendance/calendar.html', {'month': month_name, 'today_date':todays_date, 'calendar': cal_data})

# after choosing date from calendar 
# another calendar obj because iterator once consumed gets exhausted
# student's status of 7 days prior today 
# after choosing date create date object in Date Model
# for form submission take date id for today's date and
# student status using student id from POST data 
# saving the data in Attendance Model by creating object 

def ChooseDate(request,date):
    # after choosing date
    # student_list = Student.objects.all().order_by('name') # student data for student list 
    todays_date = datetime.now().date()
    new_date = datetime.strptime(date,"%Y-%m-%d").date()
    print(type(date))
    print(type(new_date))
    print('Student List')
    print(student_list)
    student_list_course = Class.objects.filter(course_id=course_id_global)
    print(student_list_course)

    start_week = todays_date - timedelta(days=7)
    end_week = start_week + timedelta(days=6)

    # Get the attendance data for the specific course and week
    attendance_data = Attendance.objects.filter(today_date__range=[start_week, end_week], course_id=course_id_global)
    # Get the list of students in the course
    

    # Create a dictionary to store attendance status for each student
    student_attendance = {student.student.id: {} for student in student_list_course}
    print(student_attendance)

    # Organize the attendance data by student ID and date
    for attendance in attendance_data:
        print(attendance)
        student_id = attendance.student_id
        print(type(student_id))
        date = str(attendance.today_date)
        student_attendance[student_id][date] = attendance.status
    print(student_attendance.keys())
    # Prepare a list of dates for the table header
    date_list = [start_week + timedelta(days=i) for i in range(7)]
    for a in student_list_course:
        print(type(a.student.id))

    if request.method == 'POST':
        # create_date = Date.objects.create(today_date = new_date)
        # date_info = Date.objects.get(today_date = new_date, id = create_date.id)
        print('***************')
        # print(type(date_info.today_date))
        # print('Date Info')
        # print(date_info.today_date)
        print(request.POST)
        for student_info in student_list:
            status_value = request.POST[str(student_info.student.id)]
            print('Student Info')
            print(student_info.student.id,status_value)
            Attendance.objects.create(today_date = new_date, student_id = student_info.student.id, status = status_value, course_id = course_id_global)
        return render(request,'calendar/student_list.html', {'att_report': date_list,'student_status': student_attendance,'student_list': student_list_course,'today_date': todays_date,'month': month_name,}) 
    else:
        return render(request, 'calendar/student_list.html', {
            'att_report': date_list,
            'student_status': student_attendance,
            'student_list': student_list_course,
            'month': month_name,
            'today_date': todays_date
        })


def Attendance_Report(request,data):

    """
    We will display all the attendance report for the chosen course
    Here we take course_id from in `data` for which we want to display the attendance report.
    Then we find the ids for the course in Data (DB). Course object will have many ids because everyday attendance is taken
    After finding ids of Course in Data(DB Table) with the help of that id we will find only those objects whose course_id matches with id of Data(DB Table) from Attendance(DB Table)
    attendance_data is a list which stores objects. It stores multiple object in a single object for which the course_id matches with id of Data(DB Table)
    We have to use double for loop to get each object. First for loop gives object which has stored multiple object. Second loop gives those multiple objects which were stored in single object.
    Basically those objects are stored in nested list. Multiple objects are stored in one single object for which the id matches and in another single object multiple objects are stored for which the id matches. 
    In conclusion, for different date attendance is stored in separate object
    """
    todays_date = datetime.now().date()
    start_week = todays_date - timedelta(days=7)
    end_week = start_week + timedelta(days=6)

    # Get the attendance data for the specific course and week
    attendance_data = Attendance.objects.filter(today_date__range=[start_week, end_week], course_id=data)
    # Get the list of students in the course
    student_list_course = Class.objects.filter(course_id=data)
    print(student_list_course)

    # Create a dictionary to store attendance status for each student
    student_attendance = {student.student.id: {} for student in student_list_course}
    print(student_attendance)

    # Organize the attendance data by student ID and date
    for attendance in attendance_data:
        print(attendance)
        student_id = attendance.student_id
        print(type(student_id))
        date = str(attendance.today_date)
        student_attendance[student_id][date] = attendance.status
    print(student_attendance.keys())
    # Prepare a list of dates for the table header
    date_list = [start_week + timedelta(days=i) for i in range(7)]
    for a in student_list_course:
        print(type(a.student.id))

    return render(request, 'calendar/att_report.html', {
        'att_report': date_list,
        'student_status': student_attendance,
        'student_list': student_list_course
    })

def Download_Report(request,data):
    print(data)
    model_data = Attendance.objects.prefetch_related('course').filter(course_id = data)
    data_list = []
    for d in model_data:
        print(d.today_date)
        data_list.append({
            'SName' : d.student.name,
            'Date' :  d.today_date,
            'Course' : d.course.title,
            'Status' : d.status
        })
        print(d.student.name, d.today_date, d.course.title, d.status)
    print(data_list)
    df = pd.DataFrame(data_list)
    print('***********')
    print(df)
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = f'attachment; filename={escape_uri_path("attendance_data.xlsx")}'
    response['Content-Transfer-Encoding'] = 'binary'
    response['Cache-Control'] = 'private, no-cache, no-store, must-revalidate'
    df.to_excel(response, index=False, engine='openpyxl')
    return response
