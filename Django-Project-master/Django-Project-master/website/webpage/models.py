from django.db import models
from django.contrib.auth.models import AbstractBaseUser, UserManager
from django.contrib.auth.models import User
# Create your models here.
class Person(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    orders = models.CharField(max_length=500,default='0')
    
    class Meta:
        db_table = "users"

class Products(models.Model):
    p_name = models.CharField(max_length=50)
    p_price = models.CharField(max_length=50)
    pdesc = models.CharField(max_length=500)
    mycusid = models.CharField(max_length=50,null=True)
    class Meta:
        db_table = "products"