# Generated by Django 5.1.3 on 2024-12-06 16:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_student_managers'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='student',
            options={},
        ),
        migrations.RemoveField(
            model_name='student',
            name='date_joined',
        ),
        migrations.RemoveField(
            model_name='student',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='student',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='student',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='student',
            name='is_staff',
        ),
        migrations.RemoveField(
            model_name='student',
            name='is_superuser',
        ),
        migrations.RemoveField(
            model_name='student',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='student',
            name='user_permissions',
        ),
    ]
