# Generated by Django 4.2.2 on 2023-07-18 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calendar_app', '0003_remove_date_course_attendance_course'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attendance',
            name='date',
        ),
        migrations.AddField(
            model_name='attendance',
            name='today_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.DeleteModel(
            name='Date',
        ),
    ]
