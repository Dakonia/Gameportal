from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=User)
def add_staff_status(sender, instance, created, **kwargs):
    if created:
        instance.is_staff = True
        instance.save()