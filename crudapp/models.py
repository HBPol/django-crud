from django.db import models

from django.conf import settings

from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    birth_date = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return self.get_full_name()
    

class Member(models.Model):
    firstname = models.CharField(max_length=40)
    lastname = models.CharField(max_length=40)
    friendname = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    file = models.FileField(upload_to='uploads/')
    def __str__(self):
        return self.firstname + " " + self.lastname
    
    
