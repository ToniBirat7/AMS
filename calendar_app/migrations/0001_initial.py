# Generated by Django 4.2.2 on 2023-07-13 02:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Attendance', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Date',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('today_date', models.DateField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Date',
                'db_table': 'Date',
            },
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('A', 'Absent'), ('P', 'Present')], max_length=30)),
                ('course', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Attendance.course')),
                ('date', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='calendar_app.date')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Attendance.student')),
            ],
            options={
                'verbose_name_plural': 'Attendance',
                'db_table': 'Attendance',
            },
        ),
    ]
