from django.db import models
import uuid
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import pre_save
from django.utils.text import slugify

# Create your models here.

class Project(models.Model):
    
    STATUS = (
        ('Not Started','Not Started'),
        ('In Progress','In Progress'),
        ('Completed','Completed'),
    )
    
    title = models.CharField(max_length=100,null=True,blank=True)
    slug = models.SlugField(unique=True,blank=True)
    description = models.TextField(max_length=3000,null=True,blank=True)
    start_date = models.DateField(auto_now_add=True,null=True,blank=True)
    end_date =  models.DateField(null=True,blank=True)
    status = models.CharField(max_length=50,choices=STATUS,null=True,blank=True)
    members = models.ManyToManyField(User)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
        
    def __str__(self):
        return self.title
    

