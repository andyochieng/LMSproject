"""
URL configuration for lms project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from .views import home,CoursesVIEW,StudentsVIEW,profile,unenroll,enroll
from . import views as mainviews
from accounts import views
cv=CoursesVIEW()
sv=StudentsVIEW()

urlpatterns = [
    path('', home, name='home'),
    path('search', cv.search, name='courses_search'),
    path('signup', sv.signup, name='signup'),
    path('login', sv.login_user, name='login'),
    path('profile', profile, name='profile'),
path('enroll/<course_id>', enroll, name='enroll'),
path('unenroll/<course_id>', unenroll, name='unenroll'),

    path('view/<course_id>', cv.view, name='courses_view'),
    path('Student/Dashboard', mainviews.dashboard, name='StudentDashboard'),
    # path('main/', include('main.urls'))
]
