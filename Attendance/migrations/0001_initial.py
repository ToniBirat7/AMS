# Generated by Django 4.2.2 on 2023-07-04 05:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('duration', models.CharField(max_length=30)),
                ('shift', models.CharField(choices=[('M', 'Morning'), ('D', 'Day')], max_length=1)),
                ('starting_date', models.DateField()),
            ],
            options={
                'verbose_name_plural': 'Courses',
                'db_table': 'Course',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('roll_no', models.IntegerField()),
                ('course_enrolled', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Attendance.course')),
            ],
            options={
                'verbose_name_plural': 'Students',
                'db_table': 'Student',
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=30)),
                ('DOB', models.DateField()),
                ('primary_number', models.CharField(max_length=10, null=True, unique=True)),
                ('secondary_number', models.CharField(max_length=10, null=True, unique=True)),
                ('sex', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=10)),
                ('my_image', models.ImageField(null=True, upload_to='profile_img/')),
                ('course', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='Attendance.course')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
