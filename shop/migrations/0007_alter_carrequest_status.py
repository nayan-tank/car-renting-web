# Generated by Django 4.1.3 on 2022-12-19 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_car_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carrequest',
            name='status',
            field=models.CharField(choices=[('Pending', 'PENDING'), ('Accepted', 'ACCEPTED'), ('Cancel', 'CANCEL')], default='PENDING', max_length=10),
        ),
    ]
