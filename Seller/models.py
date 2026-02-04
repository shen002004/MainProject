from django.db import models
from Guest.models import *
from Admin.models import *

# Create your models here.
class tbl_property(models.Model):
    property_name=models.CharField(max_length=30)
    property_description=models.CharField(max_length=30)
    propertytype_id=models.ForeignKey(tbl_propertytype,on_delete=models.CASCADE,null=True)
    property_date=models.DateField(auto_now_add=True)
    property_price=models.CharField(max_length=30)
    property_photo=models.FileField(upload_to="Assets/Property/Photo/")
    property_status=models.IntegerField(default=0)
    property_typestatus = models.IntegerField(null=True)
    seller_id=models.ForeignKey(tbl_seller,on_delete=models.CASCADE,null=True)
    renter_id=models.ForeignKey(tbl_renter,on_delete=models.CASCADE,null=True)
    place_id=models.ForeignKey(tbl_Place,on_delete=models.CASCADE)
    category_id=models.ForeignKey(tbl_category,on_delete=models.CASCADE)
    


class tbl_gallery(models.Model):
    property=models.ForeignKey(tbl_property,on_delete=models.CASCADE)
    gallery_photo=models.FileField(upload_to="Assets/Property/Gallery/")
    
    