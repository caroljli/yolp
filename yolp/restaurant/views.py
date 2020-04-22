from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

def splash(request):
    return render(request, "splash.html", {})

@login_required
def logout_view(request):
    logout(request)
    return redirect("/")

# restaurant pages

def restaurant(request):
    return render(request, "restaurant.html", {})

def view_restaurants(request):
    return render(request, "view_restaurants.html", {})

def browse(request):
    return render(request, "browse.html", {})

def category(request):
    return render(request, "category.html", {})