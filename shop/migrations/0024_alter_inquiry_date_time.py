# Generated by Django 4.1.3 on 2022-12-11 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0023_alter_complain_text_alter_feedback_feedback_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inquiry',
            name='date_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
