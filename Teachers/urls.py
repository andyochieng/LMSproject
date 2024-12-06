from django.urls import path,include
from django.shortcuts import redirect
from . import views


urlpatterns = [
    path('Dashboard', views.dashboard, name='TeacherDashboard'),
    path('SignUp', views.teacherRegistration, name='TeacherSignup'),
    path('Message', views.sendMessage, name='message'),
    path('Contents/Upload', views.UploadContent, name='ContentUpload'),
    path('Contents', views.contentStatus, name='Contents'),
    path('StudentProgress', views.getStudentProgress, name='StudentProgress'),
    path('', lambda request: redirect('TeacherDashboard', permanent=False))
    ]