from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.models import User
from user.models import Account
from restaurant.models import Restaurant
from django.contrib.auth.decorators import login_required

def splash(request):
    # if request.user.is_authenticated:
    #     return redirect("/home")
    # else:
	#     return render(request, "splash.html", {})
    return render(request, "splash.html", {})

def user_dashboard(request):
    return render(request, "user_dashboard.html", {})