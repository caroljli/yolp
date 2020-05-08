from django.db import models
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django import template
from restaurant.models import Follow, Restaurant

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    school = models.CharField(max_length=200)
    bio = models.TextField()
    time = models.DateTimeField(auto_now=True, null=True)
    following = models.ManyToManyField(Follow, related_name='following', null=True)
    picture = models.CharField(max_length=600, null=True)
    is_student = True
    is_restaurant = False

    def picture_is_not_null(self):
        if self.picture is not None:
            return True
        else:
            return False

    @property
    def follow_count(self):
        return Follow.objects.filter(user=self.user).count()
    
    def has_follows(self):
        if self.follow_count > 0:
            return True
        else:
            return False
    
    def is_following(restaurant):
        if Follow.objects.get(user=self.user, restaurant=restaurant) is not None:
            return True
        else:
            return False

class Review(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=True)

    # TODO: find a way to render all restaurants in db
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, null=True)
    time = models.DateTimeField(auto_now=True, null=True)
    title = models.CharField(max_length=200)
    body = models.TextField()
    picture = models.CharField(max_length=600, null=True)

    def get_username(self):
        return self.user.username
    
    def get_name(self):
        if self.student is not None:
            return self.student.name
        else:
            return "user"

    def get_user_picture(self):
        if self.student is not None:
            return self.student.picture
        else:
            return "picture"

    def picture_is_not_null(self):
        if self.picture is not None:
            return True
        else:
            return False