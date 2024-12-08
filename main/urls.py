from django.urls import path
from .views import home, CoursesVIEW, StudentsVIEW, profile, unenroll, enroll
from . import views as mainviews  # Alias for `main` app views
from accounts import views as accounts_views  # Alias for `accounts` app views

cv = CoursesVIEW()
sv = StudentsVIEW()

urlpatterns = [
    path('', home, name='home'),
    path('search', cv.search, name='courses_search'),
    path('signup', sv.signup, name='signup'),
    path('contact/', mainviews.contact, name='contact'),  # Use `mainviews` for `main` app views
    path('login', sv.login_user, name='login'),
    path('profile', profile, name='profile'),
    path('enroll/<course_id>', enroll, name='enroll'),
    path('unenroll/<course_id>', unenroll, name='unenroll'),
    path('view/<course_id>', cv.view, name='courses_view'),
    path('Student/Dashboard', mainviews.dashboard, name='StudentDashboard'),
    path('courses/', mainviews.courses, name='courses'),
]
