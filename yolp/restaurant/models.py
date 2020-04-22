from django.db import models
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

PRICE_CHOICES = (
    ('$','$'),
    ('$$', '$$'),
    ('$$$','$$$'),
    ('$$$$','$$$$'),
)

class Category(models.Model):
    name = models.CharField(max_length=200)

class Location(models.Model):
    name = models.CharField(max_length=200)

class Restaurant(models.Model):
    # managing user
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # restaurant details
    restaurant_name = models.CharField(max_length=200)
    price = models.CharField(max_length=4, choices=PRICE_CHOICES, default='$')
    description = models.TextField()
    address = models.CharField(max_length=200)
    school = models.CharField(max_length=200)
    categories = models.ManyToManyField(Category, blank=True)
    location = models.ForeignKey(Location, blank=True, null=True, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now=True, null=True)