from django.db import models
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from restaurant_admin.models import RestaurantAdmin

# PRICE_CHOICES = (
#     ('$','$'),
#     ('$$', '$$'),
#     ('$$$','$$$'),
#     ('$$$$','$$$$'),
# )

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)

class Location(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)

class Restaurant(models.Model):
    # managing user
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    admin = models.ForeignKey(RestaurantAdmin, on_delete=models.CASCADE, null=True)

    # restaurant details
    restaurant_name = models.CharField(max_length=200)
    price = models.CharField(max_length=4, default='$')
    description = models.TextField(null=True)
    address = models.CharField(max_length=200, null=True)
    school = models.CharField(max_length=200, null=True)
    categories = models.ManyToManyField(Category, related_name='categories', blank=True)
    location = models.ForeignKey(Location, null=True, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now=True, null=True)
    picture = models.CharField(max_length=600, null=True)
    followed_by = models.ManyToManyField(User, related_name='followed_by', blank=True)
    url = models.CharField(max_length=100, null=True)
    x_coord = models.FloatField(null=True)
    y_coord = models.FloatField(null=True)
    website = models.CharField(max_length=600, null=True)

    def picture_is_not_null(self):
        if self.picture is not None:
            return True
        else:
            return False
    
    def __iter__(self):
        self._fetch_all()
        return iter(self._result_cache)

    def __del__(self):
        self.delete()

    # @property
    # def follow_count(self):
    #     return Follow.objects.filter(restaurant=self).count()
    
    # def already_following(self):
    #     if self.follow_count > 0:
    #         return True
    #     else:
    #         return False

class Follow(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, null=True)

    def get_restaurant_name(self):
        return self.restaurant.restaurant_name
    
    def get_restaurant_price(self):
        return self.restaurant.price 
    
    def get_restaurant_school(self):
        return self.restaurant.school
