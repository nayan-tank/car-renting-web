# Generated by Django 4.1.3 on 2022-12-19 08:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='company',
            old_name='com_id',
            new_name='company_id',
        ),
    ]