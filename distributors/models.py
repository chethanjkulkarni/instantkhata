from django.db import models
from accounts.models import User, District, State

# Create your models here.
class Distributor(models.Model):
    name = models.CharField(max_length=256)
    logo = models.ImageField(upload_to='uploads/images/', null=True)
    gst_number = models.CharField(max_length=32)
    district = models.ForeignKey(to=District, on_delete=models.CASCADE)
    address = models.TextField()
    gst_entity = models.CharField(max_length=32)
    gst_state = models.ForeignKey(to=State, on_delete=models.CASCADE)
    drug_license = models.CharField(max_length=16, null=True, blank=True)
    food_license = models.CharField(max_length=32, null=True, blank=True)
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)

class Type(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=256)
    image = models.ImageField(upload_to='uploads/products/', null=True, blank=True)
    type = models.ForeignKey(to=Type, on_delete=models.CASCADE)
    distributor = models.ForeignKey(to=Distributor, on_delete=models.CASCADE)
    description = models.TextField()
    mrp = models.FloatField()
    hsn = models.CharField(max_length=16)
    base_price = models.FloatField()


class Package(models.Model):
    name = models.CharField(max_length=64)
    amount = models.FloatField()
    duration = models.IntegerField(help_text="Total months this packages will work")

    def __str__(self):
        return self.name

class Purchase(models.Model):
    distributor = models.OneToOneField(to=Distributor, on_delete=models.CASCADE)
    payment_date = models.DateField()

class Subscription(models.Model):
    distributor = models.OneToOneField(to=Distributor, on_delete=models.CASCADE)
    package = models.ForeignKey(to=Package, on_delete=models.CASCADE)
    payment_date = models.DateField()

class Due(models.Model):
    subscription = models.ForeignKey(to=Subscription, on_delete=models.CASCADE)
    due_date = models.DateField()