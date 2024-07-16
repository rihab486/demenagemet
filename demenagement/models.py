from django.db import models
from django.db.models.deletion import SET_DEFAULT
import datetime
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.conf import Settings
from django.utils.translation import gettext_lazy as _
class Client(models.Model):
    name=models.CharField(max_length=200)
    lastname=models.CharField(max_length=200)
    adresse=models.CharField(max_length=200,blank=True)
    numberphone= models.IntegerField(null=True,blank=True)

class Categories(models.Model):
    nom=models.CharField(max_length=200)

class Produit(models.Model):
    nomp=models.CharField(max_length=100)
    description=models.CharField(max_length=200 ,blank=True, null=True)      
    image=models.ImageField(upload_to='users/%Y/%m/%d/', height_field=None, width_field=None, max_length=100,default=None,verbose_name='imagee',null=True,blank=True)    
    category = models.ForeignKey('demenagement.Produit', blank=True, null=True,   on_delete=SET_DEFAULT,  default=None )                                                        
    
