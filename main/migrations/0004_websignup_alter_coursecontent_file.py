# Generated by Django 5.1.3 on 2024-12-06 10:32

import pathlib
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_coursecontent_visibletoall_alter_coursecontent_file'),
    ]

    operations = [
        migrations.CreateModel(
            name='WebSignup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100, unique=True)),
                ('first_name', models.EmailField(max_length=100, unique=True)),
                ('last_name', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('group', models.CharField(choices=[('TEACHER', 'Teacher'), ('STUDENT', 'Student'), ('ADMIN', 'Admin')], default='STUDENT', max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='coursecontent',
            name='file',
            field=models.FileField(upload_to=pathlib.PureWindowsPath('C:/Users/Admin/Desktop/lms/media/course_contents')),
        ),
    ]