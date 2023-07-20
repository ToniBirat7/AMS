from django.db import models
from django.contrib.auth.models import User

shift_choice = [
    ('M','Morning'),
    ('D','Day')
]

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
    is_student = models.BooleanField(default=True)

    def __str__(self):
        return self.user.first_name
    
    class Meta:
        db_table = 'Person'
        verbose_name_plural = 'Person'

class Course(models.Model):
    title = models.CharField(max_length=30)
    duration = models.CharField(max_length=30)
    shift = models.CharField(max_length=1, choices=shift_choice)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    
    class Meta:
        db_table = 'Course'
        verbose_name_plural = 'Courses'
        ordering = ["title"]

class Student(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name
    class Meta:
        db_table = 'Student'
        verbose_name_plural = 'Students'

class Class(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    def __str__(self):
        return self.course.title
    
    class  Meta:
        db_table = 'Class'
        verbose_name_plural = 'Classes'


