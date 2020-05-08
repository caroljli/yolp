from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.models import User
from restaurant_admin.models import RestaurantAdmin
from restaurant.models import Restaurant
from student.models import Review, Student
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
import json
from django.core import serializers

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
    picture = request.POST.get("picture")
    user = User.objects.create(username=username, password=password, email=email)
    user.set_password(password)
    user.save()
    RestaurantAdmin.objects.create(user=user, name=name, bio=bio, picture=picture)
    return redirect('/restaurant_register_complete')

# restaurant pages

def restaurant_home(request):
    user = request.user
    rest_admin = RestaurantAdmin.objects.get(user=request.user)
    restaurants = Restaurant.objects.filter(user=user)
    reviews = Review.objects.none()
    for restaurant in restaurants:
        reviews |= Review.objects.filter(restaurant=restaurant)
    return render(request, "restaurant_home.html", {"user": user, "rest_admin": rest_admin, "restaurants": restaurants, "reviews": reviews})

def restaurant_register_complete(request):
    return render(request, "restaurant_register_complete.html", {})

def admin_profile(request, username=None):
    if User.objects.get(username=username):
        user = User.objects.get(username=username)
        rest_admin = RestaurantAdmin.objects.get(user=user)
        restaurants = Restaurant.objects.filter(user=user)
        return render(request, "admin_profile.html", {"user": user, "rest_admin": rest_admin, "restaurants": restaurants})
    else:
        return render("404 user not found")

def export_reviews(request, url=None):
    restaurant = Restaurant.objects.get(url=url)
    reviews = list(Review.objects.filter(restaurant=restaurant))
    s_reviews = serializers.serialize('json', reviews)
    return HttpResponse(s_reviews, content_type="application/json")