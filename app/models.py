"""
Definition of models.
"""

from django.db import models
from django.contrib.auth.models import User

#sharing entity
class Staff(models.Model):
    staff_id = models.CharField(primary_key=True, max_length=10)
    staff_password = models.CharField(max_length=5)

    def __str__(self):
        return str(self.staff_id)

class Vendor(models.Model):
    vendor_id = models.CharField(primary_key=True, max_length=10)
    vendor_name = models.CharField(max_length=20)
    vendor_address = models.CharField(max_length=100)
    vendor_contact = models.BigIntegerField()

    def __str__(self):
        return str(self.vendor_id)

class Item(models.Model):
    item_id = models.CharField(primary_key=True, max_length=10)
    vendor_id = models.ForeignKey(Vendor,default=None, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=40)
    item_quantity = models.PositiveIntegerField()
    item_price = models.DecimalField(max_digits=8, decimal_places=2)

    # item_description = models.TextField(null=True,default=None, blank=True)
    def __str__(self):
        return str(self.item_id)

class Product(models.Model):
    product_id = models.CharField(primary_key=True, max_length=10)
    vendor_id = models.ForeignKey(Vendor,default=None, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=40)
    product_quantity = models.PositiveIntegerField()
    product_price = models.DecimalField(max_digits=8, decimal_places=2)

    # item_description = models.TextField(null=True,default=None, blank=True)
    def __str__(self):
        return str(self.product_id)

class Quotation(models.Model):
    quotation_id = models.CharField(primary_key=True, max_length=10)
    staff_id = models.ForeignKey(Staff,default=None, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product,default=None, on_delete=models.CASCADE)
    vendor_id = models.ForeignKey(Vendor,default=None, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=40)
    product_price = models.DecimalField(max_digits=8, decimal_places=2)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)
    valid_until = models.DateField()
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)
    quantity_provided = models.PositiveIntegerField()
    quotation_status = models.CharField(max_length=20)

    # item_description = models.TextField(null=True,default=None, blank=True)
    def __str__(self):
        return str(self.quotation_id)

class PurchaseOrder(models.Model):
    po_id = models.CharField(primary_key=True, max_length=10)
    item_id = models.ForeignKey(Item,default=None, on_delete=models.CASCADE)
    staff_id = models.ForeignKey(Staff,default=None, on_delete=models.CASCADE)
    quotation_id = models.ForeignKey(Quotation,default=None, on_delete=models.CASCADE)
    vendor_id = models.ForeignKey(Vendor,default=None, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=40)
    quantity_provided = models.PositiveIntegerField()
    item_price = models.DecimalField(max_digits=8, decimal_places=2)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity_needed = models.PositiveIntegerField()
    po_status = models.CharField(max_length=20)

    # item_description = models.TextField(null=True,default=None, blank=True)
    def __str__(self):
        return str(self.po_id)