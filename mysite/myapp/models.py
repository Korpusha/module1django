from django.db import models
from django.contrib.auth.models import AbstractUser


class Customer(AbstractUser):
    purse = models.IntegerField(default=10000)


class Goods(models.Model):
    name = models.CharField(max_length=120)
    description = models.CharField(max_length=500)
    price = models.IntegerField()
    amount = models.IntegerField()
