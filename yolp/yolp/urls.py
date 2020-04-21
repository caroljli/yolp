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
from restaurant.views import splash, logout_view
from student.views import student_login, student_register, student_login_view, student_register_view, student_register_complete
from restaurant_admin.views import restaurant_login, restaurant_register, restaurant_register_complete, restaurant_login_view, restaurant_register_view

urlpatterns = [
    # general
    path('admin/', admin.site.urls),
    path('', splash, name="splash"),
    path('logout_view/', logout_view, name="logout_view"),

    # restaurant admin
    path('restaurant_login/', restaurant_login, name="restaurant_login"),
    path('restaurant_register/', restaurant_register, name="restaurant_register"),
    path('restaurant_login_view/', student_login_view, name="student_login+view"),
    path('restaurant_register_view/', restaurant_login_view, name="restaurant_login_view"),
    path('restaurant_register_complete/', restaurant_register_complete, name="restaurant_register_complete"),

    # student
    path('student_login/', student_login, name="student_login"),
    path('student_register/', student_register, name="student_register"),
    path('student_login_view/', student_login_view, name="student_login+view"),
    path('student_register_view/', student_login_view, name="student_login_view"),
    path('student_register_complete/', student_register_complete, name="student_register_complete"),
   
]
