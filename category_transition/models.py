from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Transition(models.Model):
    amount_product = models.IntegerField()
    note = models.CharField(max_length=1000)

    def __str__(self):
        return f'{self.note} - {self.amount_product}'


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'
