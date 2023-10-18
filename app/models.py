from django.db import models
from django.contrib.auth.models import User

class Items(models.Model):
    brand = models.CharField(max_length=40)
    name = models.CharField(max_length=40)

class Favorites(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(Items, related_name='favorite', null=True, blank=True)
    
