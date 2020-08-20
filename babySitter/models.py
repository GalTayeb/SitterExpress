from django.db import models


class BabysitterOrders(models.Model):
    date = models.DateField(blank=True, null=True)
    b_name = models.CharField(default='', max_length=20)
    p_name = models.CharField(default='', max_length=20)
    phone_number = models.CharField(default='', max_length=10)


class ParentOrders(models.Model):
    date = models.DateField(blank=True, null=True)
    p_name = models.CharField(default='', max_length=20)
    b_name = models.CharField(default='', max_length=20)
    phone_number = models.CharField(default='', max_length=10)
    rating = models.PositiveSmallIntegerField(default=0)
