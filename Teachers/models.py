from django.db import models

class Teachers(models.Model): 
    TeacherId = models.AutoField(primary_key=True) 
    name = models.TextField(max_length=30, unique=False)
    phoneNumber= models.CharField(max_length=14, null=False, unique=True) 
    Email= models.EmailField(unique=True,null=True)
    Course=models.CharField(max_length=30)
    username=models.CharField(max_length=64,unique=True,null=False)
    password=models.CharField(max_length=64,unique=False,null=False)
    JoinDate = models.DateTimeField(auto_now_add=True) 

class Messages(models.Model): 
    timestamp = models.DateTimeField(auto_now_add=True)
    Sender = models.IntegerField(unique=False,null=False) #ID OF THE TEACHER WHO SENT
    Recepient = models.IntegerField(null=False,unique=False,default=-1) # -1 if to send to all students
    message=models.CharField(max_length=255,unique=False,null=True)
    ReadBy = models.JSONField(default=list, blank=True) #list of people who have read the sms