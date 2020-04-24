from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.models import User
from student.models import Student
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

# student authentication

def student_login(request):
    return render(request, "student_login.html", {})

def student_login_view(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(username=username, password=password)
    if user is not None:
        student = Student.objects.filter(user=user)
        if student.is_student:
            auth_login(request, user)
            return redirect("/student_home")
        else:
            return redirect("/student_login")
    else:
        return redirect("/student_login")

def student_register(request):
    return render(request, "student_register.html", {})

def student_register_view(request):
    name = request.POST["name"]
    username = request.POST["username"]
    password = request.POST["password"]
    email = request.POST["email"]
    school = request.POST["school"]
    bio = request.POST["bio"]
    user = User.objects.create(username=username, password=password, email=email)
    user.set_password(password)
    user.save()
    Student.objects.create(user=user, name=name, school=school, bio=bio)
    return redirect('/student_register_complete')

# student pages

def student_home(request):
    user = request.user
    student = Student.objects.filter(user=user)
    return render(request, "student_home.html", {"user": user, "student": student})

def student_register_complete(request):
    return render(request, "student_register_complete.html", {})

def student_profile(request):
    return render(request, "student_profile.html", {})