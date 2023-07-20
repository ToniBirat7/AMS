# Generated by Django 4.2.2 on 2023-07-13 05:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Attendance', '0001_initial'),
        ('calendar_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attendance',
            name='course',
        ),
        migrations.AddField(
            model_name='date',
            name='course',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Attendance.course'),
        ),
    ]