from django.db import models
import uuid
from django.contrib.auth.models import User


GENDER_CHOICES = [(None,"Choice one"),("Male","Male"),("Female","Female"),("Other","Other")]

class Profile(models.Model):
    
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    owner = models.OneToOneField(User,on_delete=models.CASCADE)


    first_name = models.CharField(max_length=50,blank=True,null=True)
    last_name = models.CharField(max_length=50,blank=True,null=True)

    birth_date = models.DateField(null=True,blank=True)
    gender = models.CharField(max_length=6,choices=GENDER_CHOICES,blank=True,null=True)
    phone_number = models.CharField(max_length=10,blank=True,null=True)
    address = models.CharField(max_length=100,blank=True,null=True)

    validated = models.BooleanField(default=False)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class CustomResponse(models.Model):
    message = models.CharField(max_length=200)
    token = models.CharField(max_length=50,blank=True,null=True)