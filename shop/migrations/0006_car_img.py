# Generated by Django 4.1.3 on 2022-12-19 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_car_sold_out'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='img',
            field=models.ImageField(default='images/car1.jpg', upload_to='images/'),
        ),
    ]