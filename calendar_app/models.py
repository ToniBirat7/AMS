from django.db import models
from Attendance.models import Student
# Create your models here.

class Date(models.Model):
    today_date = models.DateField(null=True,blank=True)
    def __str__(self):
        return str(self.today_date)
    class Meta:
        db_table = 'Date'
        verbose_name_plural = 'Date'

status_choice = [
        ('A','Absent'),
        ('P','Present')
    ]

class Attendance(models.Model):
    date = models.ForeignKey(Date,on_delete=models.CASCADE)
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    status = models.CharField(max_length=30,choices=status_choice)
    def __str__(self):
        return (self.student.name)
    
    class Meta:
        db_table = 'Attendance'
        verbose_name_plural = 'Attendance'


