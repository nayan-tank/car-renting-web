# Generated by Django 4.1.3 on 2022-12-11 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0017_remove_car_engine_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='car_stock',
        ),
        migrations.AddField(
            model_name='model',
            name='car_stock',
            field=models.IntegerField(default=1),
        ),
    ]
