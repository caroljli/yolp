from django.db import models
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django import template

class Student(models.Model):
    # has user field
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    school = models.CharField(max_length=200)
    bio = models.TextField()
    time = models.DateTimeField(auto_now=True, null=True)