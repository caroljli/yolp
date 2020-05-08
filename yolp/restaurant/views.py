from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.models import User
from student.models import Student, Review
from restaurant.models import Restaurant, Follow
from restaurant_admin.models import RestaurantAdmin
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

def splash(request):
    if request.user.is_authenticated:
        if Student.objects.filter(user=request.user).count() > 0:
            return redirect("/student_home")
        else:
            return redirect("/restaurant_home")
    else:
	    return render(request, "splash.html", {})
    return render(request, "splash.html", {})

@login_required
def logout_view(request):
    logout(request)
    return redirect("/")

# restaurant pages

def restaurant(request, name=None):
    if Restaurant.objects.get(restaurant_name=name):
        restaurant = Restaurant.objects.get(restaurant_name=name)
        reviews = Review.objects.filter(restaurant=restaurant.id)
        return render(request, "restaurant.html", {"restaurant": restaurant, "reviews": reviews})
    else:
        return render("404: restaurant not found")

def view_restaurants(request):
    return render(request, "view_restaurants.html", {})

def browse(request):
    return render(request, "browse.html", {})

def category(request):
    return render(request, "category.html", {})

# create new restaurant

def new_restaurant(request):
    return render(request, "new_restaurant.html", {})

def new_restaurant_view(request):
    name = request.POST.get("restaurant_name")
    school = request.POST.get("school")
    address = request.POST.get("address")
    price = request.POST.get("price")
    description = request.POST.get("description")
    picture = request.POST.get("picture")
    Restaurant.objects.create(user=request.user, admin=RestaurantAdmin.objects.get(user=request.user), restaurant_name=name, price=price, school=school, description=description, address=address, picture=picture)
    return redirect('/new_restaurant_complete')

def new_restaurant_complete(request):
    return render(request, "new_restaurant_complete.html", {})

# follow

def follow(request):
    user = request.user
    student = Student.objects.get(user=user)
    if 'follow' in request.POST:
        restaurant = Restaurant.objects.get(restaurant_name=request.POST.get('follow'))
        restaurant.followed_by.add(user)
        new_follow, created = Follow.objects.get_or_create(user=user, restaurant=restaurant)
        student.following.add(new_follow)
    else:
        restaurant = Restaurant.objects.get(restaurant_name=request.POST.get('unfollow'))
        restaurant.followed_by.remove(user)
        student.following.remove(Follow.objects.get(user=user, restaurant=restaurant))
        Follow.objects.filter(user=user, restaurant=restaurant).delete()
        
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))