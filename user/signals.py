from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User
from order.models import UserCart

@receiver(post_save, sender=User)
def create_user_cart(sender, instance, created, **kwargs):
    if created:
        UserCart.objects.create(user=instance)
