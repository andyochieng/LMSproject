from tabnanny import check

from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser
from datetime import date
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import PermissionsMixin
class StudentManager(BaseUserManager):
    """
    Custom manager for Student model.
    """

    def create_user(self, email, password=None, **extra_fields):
        """
        Create and return a regular student user.
        """
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        extra_fields.setdefault('is_active', True)
        student = self.model(email=email, **extra_fields)
        student.set_password(password)
        student.save(using=self._db)
        return student

    def create_superuser(self, email, password=None, **extra_fields):
        """
        Create and return a student with superuser privileges.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get('is_superuser') is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(email, password, **extra_fields)

# Create your models here.

# Student model
# class WebSignup(models.Model):
#     GROUPS = [
#         ('TEACHER', 'Teacher'),
#         ('STUDENT', 'Student'),
#         ('ADMIN', 'Admin')
#     ]
#     username = models.CharField(max_length=100,unique=True,null=False)
#     first_name = models.EmailField(max_length=100, unique=True,null=False)
#     last_name = models.CharField(max_length=100,null=False)
#     password = models.CharField(null=False,max_length=100)
#     group =models.CharField(max_length=100,null=False,default='STUDENT',choices=GROUPS)

#models for course
class Course(models.Model):
    category = models.CharField(max_length=50)
    teacher = models.CharField(max_length=50)
    title = models.CharField(max_length=150)
    description = models.TextField()

class CourseContent(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="contents")
    file = models.FileField(upload_to=settings.MEDIA_ROOT/"course_contents")
    title = models.CharField(max_length=255)
    visibleToAll=models.BooleanField(default=False)
    number = models.IntegerField()

    class Meta:
        ordering = ['number']  # Order contents by number

# class User(AbstractUser):
#   username = models.CharField(max_length = 50, blank = True, null = True, unique = True)
#   email = models.EmailField(_('email address'), unique = True)
#   native_name = models.CharField(max_length = 5)
#   phone_no = models.CharField(max_length = 10)
#   USERNAME_FIELD = 'email'
#   REQUIRED_FIELDS = ['username', 'first_name', 'last_name']
#   def __str__(self):
#       return "{}".format(self.email)
# Student mod
class Student(AbstractBaseUser,PermissionsMixin):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    username=None
    password = models.CharField(max_length=100)
    # mobile_no = models.CharField(max_length=20)
    courses = models.ManyToManyField(
        'Course', through='Enrollment', related_name='students'
    )
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name',]
    objects = StudentManager()


class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    progress = models.IntegerField()  # progress as percentage
    date_enrolled = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.student} in {self.course} ({self.progress}%)"

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} - {self.email}"

