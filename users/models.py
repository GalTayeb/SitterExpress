from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    GENDER_CHOICES = (
        ('', '---'),
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(default='', max_length=10, choices=GENDER_CHOICES)

    age = models.CharField(default='', max_length=3)
    id_number = models.CharField(default='', max_length=9)
    phone_number = models.CharField(default='', max_length=10)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    one_to_five_choices = zip(range(1, 5 + 1), range(1, 5 + 1))
    rating = models.PositiveSmallIntegerField(default=0, choices=one_to_five_choices)

    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name
