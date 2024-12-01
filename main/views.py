from django.shortcuts import render
from .models import  Course,CourseContent
from django.db import models

# Cre
# Create your views here.
def home(request):
    return render(request, 'main/home.html')

class StudentsVIEW:
    def signup(self,request):
        pass
    def login(self,request):
        pass
    def profile(self,request):
        """
        WE NEED TOP SHOW COURSES
        FULL NAME
        EMAIL



        :param request:
        :return:
        """
        pass
class CoursesVIEW:

    """
    BEYOND THIS POINT CAN BE DONE BY ANYONE NOT JUST ADMIN
    """

    def search(self, request):
        query = request.GET.get('q', None)  # Get the search query from the request
        if query:
            # Filter courses by name or description containing the search term
            courses = Course.objects.filter(
                models.Q(name__icontains=query) | models.Q(description__icontains=query)
            )
        else:
            # Return all courses if no query is provided
            courses = Course.objects.all()
            print(courses)


        return render(request, 'main/search.html', {'courses': courses, 'query': query})

    def view(self, request, course_id):
        course = Course.objects.get(id=course_id)
        course_contents=CourseContent.objects.filter(course=course)
        print(course_contents)
        return render(request, 'main/view.html', {'course': course,"contents":course_contents})
"""
WHAT HAPPENS WHEN SOMEONE IS TAKING A COURSE
linking surface 

"""



