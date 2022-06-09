from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(primary_key=True, max_length=200)
    price = models.FloatField()
    quantity = models.IntegerField()
    expiry = models.DateField(null=True)

