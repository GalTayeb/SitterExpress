# Generated by Django 3.0.8 on 2020-08-12 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='modelbabysitter',
            name='available',
            field=models.BooleanField(default=True),
        ),
    ]
