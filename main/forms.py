from django import forms
from .models import Student

class StudentSignupForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['full_name', 'email', 'password',]
class StudentLoginForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['email', 'password',]
"""
STUDENT FORM IS NEEDED
LOGIN 
SIGNUP

"""