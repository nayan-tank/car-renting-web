# Generated by Django 4.1.3 on 2022-12-11 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('brand_id', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('brand_name', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('com_id', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=45)),
                ('address', models.CharField(max_length=45)),
                ('contact', models.IntegerField()),
                ('email', models.CharField(max_length=45, unique=True)),
            ],
        ),
    ]