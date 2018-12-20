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
    file = models.FileField(upload_to='uploads/', blank=True) # File is automatically uploaded to MEDIA_ROOT/uploads/
   
    def __str__(self):
        return self.firstname + " " + self.lastname
    
class MyTestModel(models.Model):
    my_char = models.CharField(max_length=50)
    my_date = models.DateField()
    my_datetime = models.DateTimeField()
    my_integer = models.IntegerField()
    my_boolean = models.BooleanField()
    my_email = models.EmailField(max_length=254)
    my_text = models.TextField(max_length=500)
    my_time = models.TimeField()
    
    def __str__(self):
        return self

    
    
