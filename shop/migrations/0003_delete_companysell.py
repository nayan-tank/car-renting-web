# Generated by Django 4.1.3 on 2022-12-19 08:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_rename_com_id_company_company_id'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CompanySell',
        ),
    ]
