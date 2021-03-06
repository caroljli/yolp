"""yolp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from restaurant.views import splash, logout_view, restaurant, view_locations, browse, category, new_restaurant, new_restaurant_view, new_restaurant_complete, follow
from student.views import student_login, student_register, student_login_view, student_register_view, student_register_complete, student_home, student_profile, new_review
from restaurant_admin.views import restaurant_login, restaurant_register, restaurant_register_complete, restaurant_login_view, restaurant_register_view, restaurant_home, admin_profile, export_reviews

urlpatterns = [
    # general
    path('admin/', admin.site.urls),
    path('', splash, name="splash"),
    path('logout_view/', logout_view, name="logout_view"),

    # restaurant admin
    path('restaurant_login/', restaurant_login, name="restaurant_login"),
    path('restaurant_register/', restaurant_register, name="restaurant_register"),
    path('restaurant_login_view/', restaurant_login_view, name="restaurant_login_view"),
    path('restaurant_register_view/', restaurant_register_view, name="restaurant_register_view"),
    path('restaurant_register_complete/', restaurant_register_complete, name="restaurant_register_complete"),
    path('restaurant_home/', restaurant_home, name="restaurant_home"),
    path('export_reviews/<slug:url>', export_reviews, name="export_reviews"),

    # student
    path('student_login/', student_login, name="student_login"),
    path('student_register/', student_register, name="student_register"),
    path('student_login_view/', student_login_view, name="student_login_view"),
    path('student_register_view/', student_register_view, name="student_register_view"),
    path('student_register_complete/', student_register_complete, name="student_register_complete"),
    path('student_home/', student_home, name="student_home"),
    path('student_profile/<slug:username>', student_profile, name="student_profile"),

    path('new_review/', new_review, name="new_review"),

    # restaurant
    path('restaurant/<slug:url>', restaurant, name="restaurant"),
    path('view_locations/', view_locations, name="view_locations"),
    path('browse/<slug:id>', browse, name="browse"),
    path('admin_profile/<slug:username>', admin_profile, name="admin_profile"),
    path('category/<slug:id>', category, name="category"),
    path('new_restaurant/', new_restaurant, name="new_restaurant"),
    path('new_restaurant_view/', new_restaurant_view, name="new_restaurant_view"),
    path('new_restaurant_complete/', new_restaurant_complete, name="new_restaurant_complete"),
    path('follow/', follow, name="follow"),
]
