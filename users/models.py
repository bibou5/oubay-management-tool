from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify 


class ProfileRequest(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20)
    slug = models.SlugField(unique=True,blank=True)
    address = models.TextField()
    profile_picture = models.ImageField(upload_to='profile_pictures')
    is_approved = models.BooleanField(default=False)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.user.username)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.user.username
    



    

    