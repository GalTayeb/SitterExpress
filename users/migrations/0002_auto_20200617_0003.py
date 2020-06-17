# Generated by Django 3.0.6 on 2020-06-17 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='age',
            field=models.CharField(default='', max_length=3),
        ),
        migrations.AddField(
            model_name='profile',
            name='gender',
            field=models.CharField(choices=[('', '---'), ('M', 'Male'), ('F', 'Female')], default='', max_length=10),
        ),
        migrations.AddField(
            model_name='profile',
            name='id_number',
            field=models.CharField(default='', max_length=9),
        ),
        migrations.AddField(
            model_name='profile',
            name='phone_number',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='profile',
            name='rating',
            field=models.PositiveSmallIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=0),
        ),
    ]
