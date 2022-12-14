# Generated by Django 4.1.3 on 2022-12-24 13:35

from django.db import migrations, models
import shop.models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0012_rename_transmmision_carrequest_transmission_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='complain',
            old_name='text',
            new_name='complain_text',
        ),
        migrations.AlterField(
            model_name='carrequest',
            name='car_name',
            field=models.CharField(max_length=45, validators=[shop.models.clean_car_name]),
        ),
        migrations.AlterField(
            model_name='carrequest',
            name='color',
            field=models.CharField(max_length=10, validators=[shop.models.clean_color]),
        ),
        migrations.AlterField(
            model_name='carrequest',
            name='fuel_type',
            field=models.CharField(max_length=20, validators=[shop.models.clean_fuel_type]),
        ),
        migrations.AlterField(
            model_name='carrequest',
            name='model_name',
            field=models.CharField(max_length=45, validators=[shop.models.clean_model_name]),
        ),
        migrations.AlterField(
            model_name='carrequest',
            name='transmission',
            field=models.CharField(max_length=30, validators=[shop.models.clean_transmission]),
        ),
    ]
