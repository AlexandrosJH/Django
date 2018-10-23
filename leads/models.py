from django.db import models
from django.urls import reverse

# Create your models here.
class Lead(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    job = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
