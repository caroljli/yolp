from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.models import User
from student.models import Student, Review
from restaurant.models import Follow
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
    return render(request, "student_home.html", {"user": user, "student": student})

def student_register_complete(request):
    return render(request, "student_register_complete.html", {})

def student_profile(request):
    user = request.user
    student = Student.objects.get(user=user)
    reviews = Review.objects.filter(user=user)
    followed_restaurants = Follow.objects.filter(user=user)
    return render(request, "student_profile.html", {"user": user, "student": student, "reviews": reviews, "follows": followed_restaurants})

# posts

def new_review(request):
    if request.method == 'POST':
        title = request.POST.get('review_title')
        body = request.POST.get('review_body')
        review = Review.objects.create(title=title, body=body, user=request.user, student=Student.objects.get(user=request.user))

        # post_body = tweet.body.split(" ")
        # for n, word in enumerate(post_body):
        #     if '#' in word:
        #         word = word[1:]
        #         if not Hashtag.objects.filter(content=word).exists():
        #             hashtag = Hashtag.objects.create(content=word)
        #         else:
        #             hashtag = Hashtag.objects.get(content=word)
        #         tweet.hashtags.add(hashtag)
        #         post_body[n] = '<a href="' + '/.' + '/hashtag/' + word + '">#' + word + '</a>'

        # post_body_str = " ".join(post_body)
        # setattr(tweet, 'body', post_body_str)
        # tweet.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))