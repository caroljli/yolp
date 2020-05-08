from django.contrib import admin
from restaurant.models import Restaurant, Location, Category

admin.site.register(Restaurant)
admin.site.register(Location)
admin.site.register(Category)