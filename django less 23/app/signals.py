from django.dispatch import receiver
from django.db.models.signals import post_save, pre_delete
from .models import Profile
from django.contrib.auth.models import User
import os
from django.conf import settings


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    profile_data = kwargs.get('profile_data', {})
    if created:
        Profile.objects.create(user=instance,
        address=profile_data.get('address'),
        birthday=profile_data.get('birthday'),
        picture=profile_data.get('picture'))
    
@receiver(pre_delete, sender=User)
def delete_picture(sender, instance, created, **kwargs):
    os.remove(os.path.join(settings.BASE_DIR, instance.profile.picture))

