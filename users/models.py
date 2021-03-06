from django.contrib.auth.models import AbstractUser
from django.db import models


class ModelUser(AbstractUser):
    is_babysitter = models.BooleanField(default=False)
    is_parent = models.BooleanField(default=False)


class ModelBabysitter(ModelUser):
    user = models.OneToOneField(ModelUser, on_delete=models.CASCADE, primary_key=True)
    available = models.BooleanField(default=True)
    GENDER_CHOICES = (
        ('', '---'),
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(default='', max_length=10, choices=GENDER_CHOICES)
    age = models.CharField(default='', max_length=3)
    id_number = models.CharField(default='', max_length=9)
    phone_number = models.CharField(default='', max_length=10)
    max_kids = models.CharField(default='', max_length=1)
    salary_per_hour = models.CharField(default='', max_length=3)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    one_to_five_choices = zip(range(1, 5 + 1), range(1, 5 + 1))
    rating = models.PositiveSmallIntegerField(default=3, choices=one_to_five_choices)
    lat = models.DecimalField(max_digits=10, decimal_places=7, null=True, blank=True)
    lng = models.DecimalField(max_digits=10, decimal_places=7, null=True, blank=True)


class ModelParent(ModelUser):
    user = models.OneToOneField(ModelUser, on_delete=models.CASCADE, primary_key=True)
    GENDER_CHOICES = (
        ('', '---'),
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(default='', max_length=10, choices=GENDER_CHOICES)
    age = models.CharField(default='', max_length=3)
    id_number = models.CharField(default='', max_length=9)
    phone_number = models.CharField(default='', max_length=10)
    num_of_kids = models.CharField(default='', max_length=2)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
