from django.db import models
from django.contrib.auth.models import User

shift_choice = [
    ('M','Morning'),
    ('D','Day')
]

class Course(models.Model):
    title = models.CharField(max_length=30)
    duration = models.CharField(max_length=30)
    shift = models.CharField(max_length=1, choices=shift_choice)
    starting_date = models.DateField()

    def __str__(self):
        return self.title
    class Meta:
        db_table = 'Course'
        verbose_name_plural = 'Courses'
        ordering = ["title"]

class Course_Teacher(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.user)
    class Meta:
        db_table = 'Course_Teacher'
        verbose_name_plural = 'Course_Teacher'


class Student(models.Model):
    name = models.CharField(max_length=30)
    roll_no = models.IntegerField()
    course_enrolled = models.ForeignKey(Course, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name
    class Meta:
        db_table = 'Student'
        verbose_name_plural = 'Students'

class  Attendance(models.Model):
    status_choice = [
        ('A','Absent'),
        ('P','Present')
    ]
    date = models.DateField(auto_now_add=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    status = models.CharField(max_length=1,choices=status_choice)

    def __str__(self):
        return str(self.student)
    class Meta:
        db_table = 'Attendance'
        verbose_name_plural = 'Attendance'
        ordering = ['date','student','status']

Gender = [
    ('M','Male'),
    ('F','Female')

]

class Person(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=30)
    DOB = models.DateField()
    primary_number = models.CharField(max_length=10, null=True, unique=True)
    secondary_number = models.CharField(max_length=10, null=True, unique=True)
    sex = models.CharField(max_length=10, choices=Gender)
    my_image = models.ImageField(upload_to='profile_img/', null=True)
    def __str__(self):
        return self.user.first_name
    
    class meta:
        db_table = 'Person'
        verbose_name_plural = 'Person'




