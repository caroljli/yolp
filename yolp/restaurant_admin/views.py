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
        auth_login(request, user)
        return redirect("/restaurant_home")
    else:
        return redirect("/restaurant_login")

def restaurant_register(request):
    return render(request, "restaurant_register.html", {})

def restaurant_register_view(request):
    name = request.POST["name"]
    username = request.POST["username"]
    password = request.POST["password"]
    email = request.POST["email"]
    school = request.POST["school"]
    description = request.POST["description"]
    price = request.POST["price"]
    address = request.POST["address"]
    restaurant_name = request.POST["restaurant_name"]
    user = User.objects.create(username=username, password=password, email=email)
    user.set_password(password)
    user.save()
    RestaurantAdmin.objects.create(user=user, name=name, school=school, bio=bio)
    return redirect('/restaurant_register_complete')

# restaurant pages

def restaurant_home(request):
    return render(request, "restaurant_home.html", {})

def restaurant_register_complete(request):
    return render(request, "restaurant_register_complete.html", {})