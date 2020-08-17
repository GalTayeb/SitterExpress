from django.db import models


class Order(models.Model):
    date = models.CharField(default='', max_length=10)
    contact = models.CharField(default='', max_length=100)
    status = models.BooleanField(default=False)

    # User | Date | ContactDetails| Status
    # Order.objects.filter(user=user).filter(status=0)
