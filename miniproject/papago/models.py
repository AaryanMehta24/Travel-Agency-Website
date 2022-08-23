from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
# Create your models here.

# class Destination:
#     id : int
#     name : str
#     img : str
#     desc : str
#     price : int 

class UserDetails(models.Model):
    user_id = models.AutoField(primary_key=True) 
    user_fullname = models.TextField()
    user_name = models.TextField()
    user_password = models.TextField()
    user_contact = models.CharField(max_length=10)
    user_email = models.EmailField()

        

class DestinationDetails(models.Model):
    des_id = models.AutoField(primary_key=True)
    des_name = models.CharField(max_length=50)
    price_adult = models.IntegerField(max_length=200)
    price_child = models.IntegerField(max_length=200)
    price_infant = models.IntegerField(max_length=200)

class TravelDetails(models.Model):
    travel_id = models.AutoField(primary_key=True)
    des_id = models.ForeignKey('DestinationDetails',on_delete=models.CASCADE)
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    total_adults = models.IntegerField(null=False,blank=False)
    total_child = models.IntegerField(null=True,blank=True)
    total_infant = models.IntegerField(null=True,blank=True)
    travel_date = models.DateField(null=False,blank=False)

class TravellerDetails(models.Model):
    traveller_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    traveller_name = models.CharField(max_length= 100)
    traveller_age = models.IntegerField(max_length=10)

class PaymentDetails(models.Model):
    payment_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    payment_mode = models.CharField(max_length = 100)
    payment_amount = models.IntegerField(max_length = 200)