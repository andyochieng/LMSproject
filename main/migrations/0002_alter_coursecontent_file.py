# Generated by Django 5.1.3 on 2024-12-01 14:30

import pathlib
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursecontent',
            name='file',
            field=models.FileField(upload_to=pathlib.PureWindowsPath('C:/Users/Admin/Desktop/project new/new/lms/media/course_contents')),
        ),
    ]
