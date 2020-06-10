from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, unique=True, on_delete=models.CASCADE, null=True)
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
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        img = Image.open(self.image.path)
