from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Notification(models.Model):
    message = models.TextField()
    reciptients = models.ManyToManyField(User,related_name="notifications")
    created_at = models.DateTimeField(auto_now_add=True)
