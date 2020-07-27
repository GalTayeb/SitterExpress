# Generated by Django 3.0.6 on 2020-07-27 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(default='', max_length=10)),
                ('contact', models.CharField(default='', max_length=100)),
                ('status', models.BooleanField(default=False)),
            ],
        ),
    ]
