from django.db.models.signals import post_save
from django.contrib.auth.models import Account
from django.dispatch import receiver
from .models import Profile

from account import Account
"""@receiver(post_save, sender=Account)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)"""

from django.core.exceptions import ObjectDoesNotExist

@receiver(post_save, sender=Account)
def create_user_profile(sender, instance, created, **kwargs):
    try:
        instance.profile.save()
    except ObjectDoesNotExist:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=Account)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()


