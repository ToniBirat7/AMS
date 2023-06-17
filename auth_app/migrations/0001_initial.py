# Generated by Django 4.2.2 on 2023-06-15 02:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
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
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('is_student', models.BooleanField(default=False)),
                ('course', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='auth_app.course')),
            ],
            options={
                'verbose_name_plural': 'Teachers',
                'db_table': 'Teacher',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('roll_no', models.IntegerField()),
                ('course_enrolled', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='auth_app.course')),
            ],
            options={
                'verbose_name_plural': 'Students',
                'db_table': 'Student',
            },
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('status', models.CharField(choices=[('A', 'Absent'), ('P', 'Present')], max_length=1)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth_app.student')),
            ],
            options={
                'verbose_name_plural': 'Attendance',
                'db_table': 'Attendance',
            },
        ),
    ]
