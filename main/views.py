from django.shortcuts import render
from .models import  Course,CourseContent
from django.db import models
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from django.contrib import messages
from django.views import View
from .models import Student, Course,Enrollment
from .forms import StudentSignupForm, StudentLoginForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login,logout
from django.http import Http404
from django.contrib.auth import get_user_model
User=get_user_model()
# Create your views here.
def home(request):
    return render(request, 'main/home.html')

def dashboard(request):
    return render(request, "main/studentDashboard.html")







class StudentsVIEW():

    def signup(self, request):
        if request.method == "POST":
            # form = StudentSignupForm(request.POST)
            # if form.is_valid():
                # Hash the password before saving
                # student = form.save(commit=False)
            student = User.objects.create_user(full_name=request.POST["full_name"], email=request.POST.get('email'))
            student.password = make_password(request.POST['password'])
            student.save()
            messages.success(request, "Signup successful! Please log in.")
            return redirect('login')  # Redirect to the login page
            # else:
            #     messages.error(request, "Signup failed. Please correct the errors.")
        else:
            form = StudentSignupForm()
        return render(request, 'accounts/signup.html', {'form': form})

    def login_user(self, request):
        if request.method == "POST":
            # form = StudentLoginForm(request.POST)

            email = request.POST['email']
            password = request.POST['password']
            # print("hereee")
            user = authenticate(email=email, password=password)
            print(user)
            if user is not None:
                # if not user.is_active:  # An Already Active User
                print(login(request, user))
                print("hereee")
                print(user.full_name)
                # messages.success(request, "Login successful!")
                return redirect('profile')  # Redirect to the profile page
                # else:
                #     messages.error(request, "Invalid password.")
            else:
                print("no uyser foiund")

            # form = StudentLoginForm()
        return render(request, 'accounts/login.html', )

@login_required
def profile(request):
    try:
        print(get_user_model().objects.all())
        student=request.user
        context = {
            'full_name': student.full_name,
            'email': student.email,
            'courses': student.courses.all(),
        }
        return render(request, 'accounts/profile.html', context)
    except Student.DoesNotExist:
        messages.error(request, "Invalid session. Please log in again.")
        return redirect('login')

def logout(self, request):
    pass

class CoursesVIEW:

    """
    BEYOND THIS POINT CAN BE DONE BY ANYONE NOT JUST ADMIN
    """

    # View to enroll in a course


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

        """"
        HAVING PERSONALIZED CLASSED BAY CHECKING ON ENNROLLEMNT TO GET THE COURSE PROGRESS

        """

        course = Course.objects.get(id=course_id)
        course_contents=CourseContent.objects.filter(course=course)
        try:
            enrollment = Enrollment.objects.get(student=request.user, course=course)
        except Enrollment.DoesNotExist:
            enrollment=None
        if enrollment:
            is_enrolled=True
        else:
            is_enrolled=False
        print(course_contents)
        return render(request, 'main/view.html', {'course': course,"contents":course_contents,"is_enrolled":is_enrolled})
"""
WHAT HAPPENS WHEN SOMEONE IS TAKING A COURSE
linking surface 

"""


@login_required
def enroll( request, course_id):
    try:
        course = Course.objects.get(id=course_id)
    except Course.DoesNotExist:
        raise Http404("Course not found.")

    # Check if the student is already enrolled
    if request.user.is_authenticated:
        student = request.user

        # Check if the student is already enrolled in the course
        if student in course.students.all():
            messages.warning(request, "You are already enrolled in this course.")
            return redirect('profile')

        # Enroll the student
        Enrollment.objects.create(student=student, course=course, progress=0)
        print(Enrollment.objects.filter(student=student))
        messages.success(request, f"You have successfully enrolled in the course: {course.title}")
    else:
        messages.error(request, "You must be logged in to enroll in a course.")
        return redirect('login')  # Redirect to login page if not authenticated

    return redirect('profile')


# View to unenroll from a course
@login_required
def unenroll( request, course_id):
    try:
        course = Course.objects.get(id=course_id)
    except Course.DoesNotExist:
        raise Http404("Course not found.")

    # Get the current student
    if request.user.is_authenticated:
        student = request.user

        # Check if the student is enrolled in the course
        try:
            enrollment = Enrollment.objects.get(student=student, course=course)
            enrollment.delete()  # Unenroll the student
            messages.success(request, f"You have successfully unenrolled from the course: {course.title}")
            return redirect('profile')
        except Enrollment.DoesNotExist:
            messages.warning(request, "You are not enrolled in this course.")
    else:
        messages.error(request, "You must be logged in to unenroll from a course.")
        return redirect('login')  # Redirect to login page if not authenticated

    return redirect('profile')
#
# def enrollment(self,request):
#
# def unenrollment(self,request):
#     pass


