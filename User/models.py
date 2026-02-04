from django.db import models
from Seller.models import *
from Guest.models import *


# Create your models here.
class tbl_propertybuing(models.Model):
        propertybuying_date=models.DateField(auto_now_add=True)
        propertybuying_amount=models.CharField(max_length=30)
        propertybuying_status=models.IntegerField(default=0)
        property_id=models.ForeignKey(tbl_property,on_delete=models.CASCADE)
        user_id=models.ForeignKey(tbl_user,on_delete=models.CASCADE)



class tbl_propertybooking(models.Model):
        propertybooking_date=models.DateField(auto_now_add=True)
        propertybooking_fromdate=models.DateField(null=True)
        propertybooking_todate=models.DateField(null=True)
        propertybooking_amount=models.CharField(max_length=30)
        property_id=models.ForeignKey(tbl_property,on_delete=models.CASCADE)
        user_id=models.ForeignKey(tbl_user,on_delete=models.CASCADE)
        propertybooking_status=models.IntegerField(default=0)
        

class tbl_propertybookingpayment(models.Model):
        propertybookingpayment_date=models.DateField(auto_now_add=True)
        propertybookingpayment_amount=models.CharField(max_length=30)
        propertybookingpayment_status=models.IntegerField(default=0)
        propertybooking_id=models.ForeignKey(tbl_propertybooking,on_delete=models.CASCADE)



class tbl_complaint(models.Model):
        complaint_title=(models.CharField(max_length=100))
        complaint_content=(models.CharField(max_length=300))
        complaint_status=models.IntegerField(default=0)
        complaint_date=models.DateField(auto_now_add=True)
        complaint_reply=models.CharField(max_length=300)
        user_id=models.ForeignKey(tbl_user,on_delete=models.CASCADE,null=True)
        seller_id=models.ForeignKey(tbl_seller,on_delete=models.CASCADE,null=True)
        renter_id=models.ForeignKey(tbl_renter,on_delete=models.CASCADE,null=True)

class tbl_feedback(models.Model):
        feedback_content=(models.CharField(max_length=300))
        user_id=models.ForeignKey(tbl_user,on_delete=models.CASCADE,null=True)
        seller_id=models.ForeignKey(tbl_seller,on_delete=models.CASCADE,null=True)
        renter_id=models.ForeignKey(tbl_renter,on_delete=models.CASCADE,null=True)







