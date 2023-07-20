from django.db import models
from Attendance.models import Student,Course
# Create your models here.


status_choice = [
        ('A','Absent'),
        ('P','Present')
    ]

class Attendance(models.Model):
    today_date = models.DateField(null=True,blank=True)
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    status = models.CharField(max_length=30,choices=status_choice)
    course = models.ForeignKey(Course,on_delete=models.CASCADE, null=True)

    def __str__(self):
        return (self.student.name)
    
    class Meta:
        db_table = 'Attendance'
        verbose_name_plural = 'Attendance'


