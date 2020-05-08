from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.models import User
from student.models import Student, Review
from restaurant.models import Follow, Restaurant
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

# student authentication

def student_login(request):
    return render(request, "student_login.html", {})

def student_login_view(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(username=username, password=password)
    if user is not None:
        student = Student.objects.get(user=user)
        if student.is_student is True:
            auth_login(request, user)
            return redirect("/student_home")
        else:
            return redirect("/student_login")
    else:
        return redirect("/student_login")

def student_register(request):
    return render(request, "student_register.html", {})

def student_register_view(request):
    name = request.POST.get("name")
    username = request.POST.get("username")
    password = request.POST.get("password")
    email = request.POST.get("email")
    school = request.POST.get("school")
    bio = request.POST.get("bio")
    picture = request.POST.get("picture")
    user = User.objects.create(username=username, password=password, email=email)
    user.set_password(password)
    user.save()
    Student.objects.create(user=user, name=name, school=school, bio=bio, picture=picture)
    return redirect('/student_register_complete')

# student pages
def student_home(request):
    user = request.user
    student = Student.objects.get(user=request.user)
    follows = Follow.objects.filter(user=user)
    reviews = Review.objects.none()
    for follow in follows:
        reviews |= Review.objects.filter(restaurant=follow.restaurant)
    return render(request, "student_home.html", {"user": user, "student": student, "reviews": reviews})

def student_register_complete(request):
    return render(request, "student_register_complete.html", {})

def student_profile(request, username=None):
    if User.objects.get(username=username):
        user = User.objects.get(username=username)
        student = Student.objects.get(user=user)
        reviews = Review.objects.filter(user=user)
        followed_restaurants = Follow.objects.filter(user=user)
        return render(request, "student_profile.html", {"user": user, "student": student, "reviews": reviews, "follows": followed_restaurants})
    else:
        return HttpResponseNotFound()

# posts

def new_review(request):
    if request.method == 'POST':
        title = request.POST.get('review_title')
        body = request.POST.get('review_body')
        restaurant_name = request.POST.get('restaurant')
        review_photo = request.POST.get('review_photo')
        if Restaurant.objects.get(restaurant_name=restaurant_name) is None:
            return HttpTesponseNotFound()
        else:
            restaurant = Restaurant.objects.get(restaurant_name=restaurant_name)
            review = Review.objects.create(title=title, body=body, user=request.user, student=Student.objects.get(user=request.user), restaurant=restaurant, picture=review_photo)
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    