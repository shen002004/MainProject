from django.db import models

# Create your models here.
class tbl_district(models.Model):
    district_name=models.CharField(max_length=30)
    
class tbl_category(models.Model):
    category_name=models.CharField(max_length=30)

class tbl_admin(models.Model):
    admin_name=models.CharField(max_length=30)
    admin_email=models.CharField(max_length=30)
    admin_contact=models.CharField(max_length=30)
    admin_password=models.CharField(max_length=30)

class tbl_Place(models.Model):
    place_name=models.CharField(max_length=50)
    district=models.ForeignKey('tbl_district',on_delete=models.CASCADE)
    
class tbl_Subcategory(models.Model):
    subcategory_name=models.CharField(max_length=30)
    category=models.ForeignKey('tbl_category',on_delete=models.CASCADE)

class tbl_propertytype(models.Model):
    propertytype_name=models.CharField(max_length=30)

class tbl_bhk(models.Model):
    bhk_name=models.CharField(max_length=30)
    propertytype=models.ForeignKey('tbl_propertytype',on_delete=models.CASCADE,null=True)

class tbl_furnish(models.Model):
    furnish_name=models.CharField(max_length=30)
    propertytype=models.ForeignKey('tbl_propertytype',on_delete=models.CASCADE,null=True)


    
