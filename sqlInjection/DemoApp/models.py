from django.db import models
from django.contrib.auth.models import User
from django.db import models
# Create your models here.
class UserProfile(models.Model):
    username= models.CharField(max_length=20,null=True,blank=True)
    password = models.CharField(max_length=20,null=True,blank=True)
    balance = models.IntegerField(default=0,null=True,blank=True)
    def __str__(self):
        return f"{self.user.username}'s Profile"