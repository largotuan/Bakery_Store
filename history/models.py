from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class History(models.Model):
    inventory_quantity = models.IntegerField(null=False)
    add_quantity = models.IntegerField(null=True)
    expired_quantity = models.IntegerField(null=True)
    price = models.FloatField()
    date_product = models.DateField(null=False)

    def __str__(self):
        return f'{self.inventory_quantity} - {self.price}'
