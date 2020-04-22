from django.db import models
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django import template

PRICE_CHOICES = (
    ('$','$'),
    ('$$', '$$'),
    ('$$$','$$$'),
    ('$$$$','$$$$'),
)

class RestaurantAdmin(models.Model):
    # has user field
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    restaurant_name = models.CharField(max_length=200)
    school = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    price = models.CharField(max_length=4, choices=PRICE_CHOICES, default='$')
    description = models.TextField()
    time = models.DateTimeField(auto_now=True, null=True)
    is_student = False
    is_restaurant = True