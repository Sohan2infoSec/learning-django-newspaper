from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)    
    #s_id = models.CharField(max_length=11)
    #fullname = models.CharField(max_length=30)
