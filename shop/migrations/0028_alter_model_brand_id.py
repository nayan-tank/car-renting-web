# Generated by Django 4.1.3 on 2022-12-14 10:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0027_alter_user_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='model',
            name='brand_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.brand'),
        ),
    ]