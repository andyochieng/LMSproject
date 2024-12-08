from django import forms
from Teachers.models import Teachers
from .models import (Student,Course)
from .models import ContactMessage
# ,WebSignup)

# class WebSignupForm(forms.ModelForm):
#     class Meta:
#         model = WebSignup
#         fields = ['username', 'first_name', 'last_name','password','group']

class StudentSignupForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['full_name', 'email', 'password',]
        
class StudentLoginForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['email', 'password',]

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'phone', 'message']
"""
STUDENT FORM IS NEEDED
LOGIN 
SIGNUP

# """
# class TeacherRegistrationForm(forms.ModelForm):
#     name = forms.CharField(label='Name', widget=forms.Textarea)
#     phoneNumber= forms.CharField(max_length=14, label="PhoneNumber", required=False)
#     Email= forms.EmailField(label="Email",required=False)
#     Course=forms.CharField(label="Course",max_length=30,required=True)
#     password=forms.CharField(label="Course",max_length=64)
#
# class TeacherLoginForm(forms.ModelForm):
#     class Meta:
#         model = Teachers
#         fields = ['username', 'password',]
#
# class MessageForm(forms.ModelForm):
#     recipient = forms.ModelChoiceField(queryset=Student.objects.all(), label='Recipient', required=False)
#     message = forms.CharField(label='Message', widget=forms.Textarea)
#     sendToAll = forms.BooleanField(label='Send to all recipients', required=False)
#
#
# class ContentSend(forms.ModelForm):
#     category=forms.ModelChoiceField(queryset=Course.objects.all(),label="Select Category of content",required=True)
#     sendToAll = forms.BooleanField(label='Send to Non-Enrolled', required=True)
#     title= forms.CharField(label='Title')
#     attachment = forms.FileField(label='Attachment', required=True)