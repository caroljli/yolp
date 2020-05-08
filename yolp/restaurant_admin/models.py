from django.db import models
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django import template

# PRICE_CHOICES = (
#     ('$','$'),
#     ('$$', '$$'),
#     ('$$$','$$$'),
#     ('$$$$','$$$$'),
# )

class RestaurantAdmin(models.Model):
    # has user field
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    time = models.DateTimeField(auto_now=True, null=True)
    bio = models.TextField()
    picture = models.CharField(max_length=600, null=True)
    is_student = False
    is_restaurant = True