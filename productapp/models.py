from django.db import models

# Create your models here.
class Product(models.Model):
    productname = models.CharField(max_length=255,null=True)
    productdescription = models.CharField(max_length=255,null=True)
    productquantity = models.CharField(max_length=255,null=True)
    productprice = models.CharField(max_length=255,null=True)