from django.db import models
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django import template
from restaurant.models import Restaurant

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    school = models.CharField(max_length=200)
    bio = models.TextField()
    time = models.DateTimeField(auto_now=True, null=True)
    is_student = True
    is_restaurant = False

class Review(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=True)
    # TODO: find a way to render all restaurants in db
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, null=True)
    time = models.DateTimeField(auto_now=True, null=True)
    title = models.CharField(max_length=200)
    body = models.TextField()