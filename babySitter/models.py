from django.db import models


class BabysitterOrders(models.Model):
    date = models.DateField(blank=True, default='', null=True)
    name = models.CharField(default='', max_length=20)
    phone_number = models.CharField(default='', max_length=10)
    rating = models.PositiveSmallIntegerField(default=0)


class ParentOrders(models.Model):
    date = models.DateField(blank=True, default='', null=True)
    name = models.CharField(default='', max_length=20)
    phone_number = models.CharField(default='', max_length=10)
    rating = models.PositiveSmallIntegerField(default=0)
