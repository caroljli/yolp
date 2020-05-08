from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.models import User
from student.models import Student, Review
from restaurant.models import Restaurant, Follow, Location, Category
from restaurant_admin.models import RestaurantAdmin
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from geopy.geocoders import Nominatim

# logistical

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

def restaurant(request, url=None):
    if Restaurant.objects.get(url=url):
        restaurant = Restaurant.objects.get(url=url)
        reviews = Review.objects.filter(restaurant=restaurant.id)
        categories = restaurant.categories.all()
        return render(request, "restaurant.html", {"restaurant": restaurant, "reviews": reviews, "categories": categories})
    else:
        return render("404: restaurant not found")

def browse(request, id=None):
    location = Location.objects.get(id=id)
    restaurants = Restaurant.objects.filter(location=location)
    return render(request, "browse.html", {"restaurants": restaurants, "location": location})

def view_locations(request):
    locations = Location.objects.all()
    return render(request, "view_restaurants.html", {"locations": locations})

def category(request, id=None):
    category = Category.objects.get(id=id)
    restaurants = Restaurant.objects.filter(categories__id=category.id)
    return render(request, "category.html", {"category": category, "restaurants": restaurants})

# create new restaurant

def new_restaurant(request):
    return render(request, "new_restaurant.html", {})

def new_restaurant_view(request):
    geolocator = Nominatim(user_agent="yolp")

    name = request.POST.get("restaurant_name")
    school = request.POST.get("school")
    address = request.POST.get("address")
    price = request.POST.get("price")
    description = request.POST.get("description")
    picture = request.POST.get("picture")
    location, created = Location.objects.get_or_create(name=school)
    categories = request.POST.get("categories")
    url = request.POST.get("url")
    website = request.POST.get("website")

    temp_loc = geolocator.geocode(address)
    y_coord = temp_loc.longitude
    x_coord = temp_loc.latitude

    restaurant = Restaurant.objects.create(user=request.user, 
                                           admin=RestaurantAdmin.objects.get(user=request.user), 
                                           restaurant_name=name, price=price, school=school, 
                                           description=description, address=address, 
                                           picture=picture, location=location, 
                                           url=url, website=website,
                                           x_coord=x_coord,
                                           y_coord=y_coord)

    category_body = categories.split(",")

    for n, category in enumerate(category_body):
        category.replace(" ", "")
        new_category, created = Category.objects.get_or_create(name=category)
        restaurant.categories.add(new_category)

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