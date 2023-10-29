from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import *
from django.shortcuts import get_object_or_404

@receiver(post_save, sender=User)
def create_favorites(sender, created, instance, **kwargs):
    if created:
        Favorites.objects.create(user=instance)

@receiver(post_save, sender=User)
def update_favorites(sender, created, instance, **kwargs):
    Favorites.objects.get_or_create(user=instance)

@receiver(pre_delete, sender=User)
def delete_favorites(sender, instance, *args, **kwargs):
    Favorites.objects.get(user=instance)