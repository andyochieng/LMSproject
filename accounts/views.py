from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from main.forms import StudentSignupForm
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth import get_user_model

from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

def accCreation(request):#create web acc
    if request.method == "POST":
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name =request.POST.get('last_name')
        password = make_password(request.POST.get('password'))
        group = str(request.POST.get('group')).strip().upper()

        webAccCreate = User.objects.create_user(username=username, first_name=first_name, last_name=last_name,
                                                 password=password,email=request.POST.get('email'))
        webAccCreate.save()

        user = User.objects.get(username=username)
        group = Group.objects.get(name=group)
        user.groups.add(group)

        #return JsonResponse({"status":"userAdded","message":f"{username} {first_name} {last_name} {password} {group}"})
        return redirect('login')




    elif request.method == "GET":
        # If GET request, just create an empty form
        webSignupForm = WebSignupForm()
        # Render the signup page with the form
    return render(request, 'accounts/signup.html', {'form': webSignupForm})

def accLogin(request):
    if request.method == "POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user is not None:
            if not user.is_active: #An Already Active User
                login(request,user)

            print(f"{username} logged in")

            userInfo=User.objects.get(username=username)


            if userInfo.groups.filter(name="STUDENT").exists():
                return redirect('StudentDashboard')
            elif userInfo.groups.filter(name="TEACHER").exists():
                return redirect('TeacherDashboard')
            elif userInfo.groups.filter(name="ADMIN").exists():
                return redirect('home')

        return JsonResponse({'error':'Invalid Credentials'})




    else:
        return render(request, 'accounts/login.html')

def signup(request):
    # Check if the form has been submitted
    if request.method == "POST":
        # Initialize the form with POST data
        form = StudentSignupForm(request.POST)

        # Check if the form is valid
        if form.is_valid():
            # Hash the password before saving
            student = form.save(commit=False)
            student.password = make_password(form.cleaned_data['password'])
            student.save()

            # Display success message and redirect to the login page
            messages.success(request, "Signup successful! Please log in.")
            return redirect('login')  # Redirect to the login page

        else:
            # If form is not valid, display error messages
            messages.error(request, "Signup failed. Please correct the errors.")
    else:
        # If GET request, just create an empty form
        form = StudentSignupForm()

    # Render the signup page with the form
    return render(request, 'accounts/signup.html', {'form': form})
