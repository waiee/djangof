"""
Definition of models.
"""

from django.db import models

from django.contrib.auth.models import User

#sharing entity

class Vendor(models.Model):
    vendor_id = models.CharField(primary_key=True, max_length=10)
    vendor_name = models.CharField(max_length=100)
    vendor_address = models.CharField(max_length=200)
    vendor_contact = models.BigIntegerField()
    
    def __str__(self):
        return str(self.item_id)

class Item(models.Model):
    item_id = models.CharField(primary_key=True, max_length=10)
    vendor_id = models.ForeignKey(Vendor,default=None, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=100)
    item_name =  models.CharField(max_length=100)
    item_quantity =  models.BigIntegerField()
    item_price = models.BigIntegerField()

    # item_description = models.TextField(null=True,default=None, blank=True)
    def __str__(self):
        return str(self.item_id)