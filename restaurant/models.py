from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price_range = models.IntegerField()
    rating = models.IntegerField()
