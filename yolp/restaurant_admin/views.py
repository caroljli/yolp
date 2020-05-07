from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.models import User
from restaurant_admin.models import RestaurantAdmin
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

# restaurant authentication

def restaurant_login(request):
    return render(request, "restaurant_login.html", {})

def restaurant_login_view(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(username=username, password=password)
    if user is not None:
        rest_admin = RestaurantAdmin.objects.get(user=user)
        if rest_admin.is_restaurant is True:
            auth_login(request, user)
            return redirect("/restaurant_home")
        else:
            return redirect("/restaurant_login")
    else:
        return redirect("/restaurant_login")

def restaurant_register(request):
    return render(request, "restaurant_register.html", {})

def restaurant_register_view(request):
    name = request.POST.get("name")
    username = request.POST.get("username")
    password = request.POST.get("password")
    email = request.POST.get("email")
    bio = request.POST.get("bio")
    user = User.objects.create(username=username, password=password, email=email)
    user.set_password(password)
    user.save()
    RestaurantAdmin.objects.create(user=user, name=name, bio=bio)
    return redirect('/restaurant_register_complete')

# restaurant pages

def restaurant_home(request):
    user = request.user
    rest_admin = RestaurantAdmin.objects.get(user=request.user)
    return render(request, "restaurant_home.html", {"user": user, "rest_admin": rest_admin})

def restaurant_register_complete(request):
    return render(request, "restaurant_register_complete.html", {})

def admin_profile(request):
    user = request.user
    rest_admin = RestaurantAdmin.objects.get(user=user)
    return render(request, "admin_profile.html", {"user": user, "rest_admin": rest_admin})