from django.db import models
from projects.models import Project
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):
    
    PRIORITY_LEVEL = (
        ('Low','Low'),
        ('Medium','Medium'),
        ('High','High'),
    )
    
    STATUS = (
        ('Not Started','Not Started'),
        ('In Progress','In Progress'),
        ('Completed','Completed'),
    )
    
    title = models.CharField(max_length=100,null=True,blank=True) 
    description = models.TextField(max_length=500,null=True,blank=True)
    due_date = models.DateField(null=True,blank=True)
    priority_level = models.CharField(max_length=50,choices=PRIORITY_LEVEL,null=True,blank=True)
    status = models.CharField(max_length=50,choices=STATUS,null=True,blank=True)
    project = models.ForeignKey(Project,on_delete=models.CASCADE)
    assigned_to = models.ManyToManyField(User)
    
    def __str__(self):
        return self.title