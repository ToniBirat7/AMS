from django.urls import path, include
from . import views
urlpatterns = [
    path('display-calendar/<int:course_id>',views.Display_Calendar, name="display-calendar"),
    path('<str:date>/', views.ChooseDate, name="date-choose"),
    path('attendance-report/<int:data>/', views.Attendance_Report, name="attendance-report"),
    path('<int:data>', views.Download_Report, name="download-report"),
]