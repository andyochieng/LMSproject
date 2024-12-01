from django.db import models
from django.conf import settings
# Create your models here.

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
    number = models.IntegerField()

    class Meta:
        ordering = ['number']  # Order contents by number


# Student model
class Student(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    # mobile_no = models.CharField(max_length=20)
    courses = models.ManyToManyField(
        'Course', through='Enrollment', related_name='students'
    )


class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    progress = models.IntegerField()  # progress as percentage
    date_enrolled = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.student} in {self.course} ({self.progress}%)"

