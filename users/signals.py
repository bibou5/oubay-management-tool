from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import Group
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def assign_to_simple_user_group(sender, instance, created, **kwargs):
    if created:
        group = Group.objects.get(name='Simple User')
        instance.groups.add(group)
