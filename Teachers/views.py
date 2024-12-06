from django.shortcuts import render,redirect
from .models import Messages,Teachers
from main.models import Student,Course,CourseContent,Enrollment
from main.forms import MessageForm,ContentSend,TeacherRegistrationForm,TeacherLoginForm
from django.http import JsonResponse,HttpResponseRedirect,Http404
import json
from django.contrib.auth.hashers import make_password, check_password
from django.contrib import messages

def dashboard(request):
    return render(request,'teacher/teacherDashboard.html')

def teacherRegistration(request):
    try:

        if request.method == "POST":
            regForm=TeacherRegistrationForm(request.POST)
            if regForm.is_valid():
                name = regForm.cleaned_data['name'] 
                phoneNumber= regForm.cleaned_data['phoneNumber'] 
                Email=regForm.cleaned_data['Email'] 
                Course=regForm.cleaned_data['Course'] 
                password=regForm.cleaned_data['password'] 
                username=regForm.cleaned_data['username']

            #REGISTER TEACHER
            Teachers.objects.create(
                name = name,
                phoneNumber= phoneNumber,
                Email=Email,
                Course=Course,
                password=password,
                username=username
            )

            return render(request,'teacher/teacherDashboard.html')
        else:
            regForm=TeacherRegistrationForm()
            return render(request,'teacher/teacherRegistration,html',{"form":regForm})
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)})


    
#SEND MESSAGES(INDIVIDUAL OR ALL)
def sendMessage(request):
    if request.method == "POST":
        teacherid=1 #for testing

        form = MessageForm(request.POST) 
        if form.is_valid():
            message = form.cleaned_data['message'] 
            sendToAll = form.cleaned_data['sendToAll']

            if sendToAll:
                recepientId = -1
            else:
                recepientId=form.cleaned_data['recipient']

        #add message
        Messages.objects.create(    
            Sender = teacherid,
            Recepient = recepientId,
            message=message
            )
        
        return render(request,'teacher/sendSms.html')
    
    else:
        form=MessageForm()
        return render(request,'teacher/sendSms.html',{"form":form})

#UPLOAD CONTENT ACCODRING TO CATEGORY (SHOW TO ANYONE IF STATUS TRUE,SHOW TO ENROLED STUDENTS IF STATUS = FALSE)
def UploadContent(request):
    if request.method == "POST":
        FormGot=ContentSend(request.POST)

        if FormGot.is_valid():
            courseTitle=FormGot.cleaned_data['category']
            sendToAll = FormGot.cleaned_data['sendToAll']
            attachment = FormGot.cleaned_data['attachment']
            title=FormGot.cleaned_data['title']

            CourseContent.objects.create(
                course = courseTitle,
                file = attachment,
                title = title,
                visibleToAll=sendToAll
            )
        
        return render(request,"teacher/ContentUpload.html")


    else:
        ContentForm=ContentSend()
        return render(request,"teacher/ContentUpload.html",{"UploadForm":ContentForm})

#CAN SEE TOTAL ENROLED STUDENTS AND THEIR PROGRESS
def getStudentProgress(request):

    if request.method=="GET":
        teacherid=1 #for testing

        teacherInfo=Teachers.objects.get(TeacherId=teacherid)
        EnrlStudents=Enrollment.objects.filter(course=teacherInfo.Course)
        return render(request,"teacher/StudentProgress.html",{"StudentInfo":EnrlStudents})
    
    else:
        return Http404("Methord not supported")


#COUNT TOTAL VIEWS OF CONTENT

def contentStatus(request):
    if request.method == "GET":
        teacherid=1 #for testing

        teacherInfo=Teachers.objects.get(TeacherId=teacherid)
        teacherContent=CourseContent.objects.filter(course=teacherInfo.Course)
       
        return render(request,"teacher/teacherContent.html",{"TeacherContent":teacherContent})

    
    else:
        return Http404("Methord not supported")
