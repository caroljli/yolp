from django.db import models
from django.db import models
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from restaurant.models import Restaurant

class Account(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    time = models.DateTimeField(auto_now=True, null=True)
    location = models.CharField(max_length=200)
    # student fields
    school = models.CharField(max_length=200, null=True, blank=True)
    grade = models.CharField(max_length=200, null=True, blank=True)
    # restaurant user fields
    restaurants = models.ManyToManyField(Restaurant, related_name='restaurant', blank=True)
