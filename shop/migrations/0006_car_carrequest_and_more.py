# Generated by Django 4.1.3 on 2022-12-11 10:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_brand_company'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('car_id', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('car_name', models.CharField(max_length=45)),
                ('price', models.IntegerField()),
                ('color', models.CharField(max_length=10)),
                ('reg_num', models.CharField(max_length=10)),
                ('km_driven', models.IntegerField()),
                ('seats', models.IntegerField()),
                ('fuel_type', models.CharField(max_length=10)),
                ('engine_type', models.CharField(max_length=45)),
                ('purc_date', models.DateField()),
                ('car_stock', models.IntegerField()),
                ('no_of_owner', models.IntegerField()),
                ('transmission', models.CharField(max_length=30)),
                ('company_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='shop.company')),
            ],
        ),
        migrations.CreateModel(
            name='CarRequest',
            fields=[
                ('car_request_id', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('car_name', models.CharField(max_length=45)),
                ('car_price', models.IntegerField()),
                ('fuel_type', models.CharField(max_length=20)),
                ('status', models.CharField(max_length=10)),
                ('color', models.CharField(max_length=10)),
                ('km_driven', models.IntegerField()),
                ('model_name', models.CharField(max_length=45)),
                ('transmmision', models.CharField(max_length=30)),
            ],
        ),
        migrations.RenameField(
            model_name='admin',
            old_name='area_area_pincode',
            new_name='area_pincode',
        ),
        migrations.RenameField(
            model_name='area',
            old_name='city_city',
            new_name='city_id',
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=10)),
                ('last_name', models.CharField(max_length=10)),
                ('email', models.CharField(max_length=45)),
                ('password', models.CharField(max_length=20)),
                ('phone', models.IntegerField()),
                ('area_pincode', models.ForeignKey(db_column='area_area_pincode', on_delete=django.db.models.deletion.DO_NOTHING, to='shop.area')),
                ('company_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='shop.company')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('pay_id', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('amount', models.IntegerField()),
                ('date_time', models.DateTimeField()),
                ('car_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='shop.car')),
                ('user_user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='shop.user')),
            ],
        ),
        migrations.CreateModel(
            name='Model',
            fields=[
                ('model_id', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('model_name', models.CharField(max_length=45)),
                ('model_no', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=200)),
                ('brand_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='shop.brand')),
            ],
        ),
        migrations.CreateModel(
            name='Inquiry',
            fields=[
                ('inquiry_id', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('inq_text', models.CharField(max_length=300)),
                ('date_time', models.DateTimeField()),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='shop.user')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('image_id', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('image_path', models.CharField(max_length=100)),
                ('car_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='shop.car')),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('feedback_id', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('feedback_text', models.CharField(max_length=300)),
                ('date_time', models.DateTimeField()),
                ('car_car', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='shop.car')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='shop.user')),
            ],
        ),
        migrations.CreateModel(
            name='Complain',
            fields=[
                ('comp_id', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('text', models.CharField(max_length=200)),
                ('date_time', models.DateTimeField()),
                ('car_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='shop.car')),
                ('user_user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='shop.user')),
            ],
        ),
        migrations.CreateModel(
            name='CompanySell',
            fields=[
                ('car_sell_id', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('sell_date', models.DateField()),
                ('company_com_id', models.CharField(max_length=5)),
                ('car_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='shop.car')),
                ('user_user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='shop.user')),
            ],
        ),
        migrations.CreateModel(
            name='CompanyPurchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purc_date', models.DateField()),
                ('car_request_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='shop.carrequest')),
                ('user_user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='shop.user')),
            ],
        ),
        migrations.AddField(
            model_name='carrequest',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='shop.user'),
        ),
        migrations.CreateModel(
            name='CarParts',
            fields=[
                ('car_parts_id', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('part_name', models.CharField(max_length=45)),
                ('price', models.IntegerField()),
                ('car_request_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='shop.carrequest')),
            ],
        ),
        migrations.AddField(
            model_name='car',
            name='model_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='shop.model'),
        ),
    ]