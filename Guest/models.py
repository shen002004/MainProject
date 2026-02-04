from django.db import models
from Admin.models import *

# Create your models here.
class tbl_user(models.Model):
    user_name=models.CharField(max_length=30)
    user_email=models.CharField(max_length=30)
    user_contact=models.CharField(max_length=30)
    user_address=models.CharField(max_length=100)
    place=models.ForeignKey(tbl_Place,on_delete=models.CASCADE)
    user_photo=models.FileField(upload_to="Assets/User/")
    user_password=models.CharField(max_length=30)
    user_status =models.IntegerField(default=0)
    
    
class tbl_seller(models.Model):
    seller_name=models.CharField(max_length=30)
    seller_email=models.CharField(max_length=30)
    seller_contact=models.CharField(max_length=30)
    seller_address=models.CharField(max_length=100)
    place=models.ForeignKey(tbl_Place,on_delete=models.CASCADE)
    seller_photo=models.FileField(upload_to="Assets/User/")
    seller_proof=models.FileField(upload_to="Assets/User/")
    seller_password=models.CharField(max_length=30)
    seller_status =models.IntegerField(default=0)
    
    
    
class tbl_renter(models.Model):
    renter_name=models.CharField(max_length=30)
    renter_email=models.CharField(max_length=30)
    renter_contact=models.CharField(max_length=30)
    renter_address=models.CharField(max_length=100)
    place=models.ForeignKey(tbl_Place,on_delete=models.CASCADE)
    renter_photo=models.FileField(upload_to="Assets/User/")
    renter_proof=models.FileField(upload_to="Assets/User/")
    renter_password=models.CharField(max_length=30)
    renter_status =models.IntegerField(default=0)    
    
    
    
    
    

    