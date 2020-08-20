# Generated by Django 3.0.8 on 2020-08-20 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BabysitterOrders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, null=True)),
                ('b_name', models.CharField(default='', max_length=20)),
                ('p_name', models.CharField(default='', max_length=20)),
                ('phone_number', models.CharField(default='', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='ParentOrders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, null=True)),
                ('p_name', models.CharField(default='', max_length=20)),
                ('b_name', models.CharField(default='', max_length=20)),
                ('phone_number', models.CharField(default='', max_length=10)),
                ('rating', models.PositiveSmallIntegerField(default=0)),
            ],
        ),
    ]
