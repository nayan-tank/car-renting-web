from django.db import models
import datetime
from django.core.validators import MaxValueValidator, MinValueValidator
# import uuid

class Admin(models.Model):
    # admin_id = models.UUIDField(auto_created=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    phone = models.CharField(max_length=10)
    email = models.CharField(unique=True, max_length=30)
    password = models.CharField(max_length=20)
    area = models.CharField(max_length=50, null=True)
    # area_pincode = models.ForeignKey('Area', null=True, on_delete=models.SET_NULL, db_column='area_area_pincode')

    def __str__(self):
        return self.first_name + ' ' + self.last_name
    


class City(models.Model):
    city_id = models.AutoField(primary_key=True, )
    city_name = models.CharField(max_length=20)

    def __str__(self):
        return self.city_name
    


class Area(models.Model):
    area_pincode = models.CharField(primary_key=True, max_length=6)
    area_name = models.CharField(max_length=45)
    city_id = models.ForeignKey('City', null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.area_name
    


class Brand(models.Model):
    brand_id = models.AutoField(primary_key=True, )
    brand_name = models.CharField(max_length=45)

    def __str__(self):
        return self.brand_name
    


class Model(models.Model):
    model_id = models.AutoField(primary_key=True, )
    model_name = models.CharField(max_length=45)
    year = models.CharField(max_length=4, default=datetime.datetime.now().strftime('%Y'))
    engine = models.CharField(max_length=30)
    car_stock = models.IntegerField(default=1)
    description = models.CharField(max_length=200)
    brand_id = models.ForeignKey(Brand, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.model_name 
    


class Company(models.Model):
    com_id = models.AutoField(primary_key=True, )
    name = models.CharField(max_length=45)
    address = models.CharField(max_length=45)
    contact = models.CharField(max_length=10)
    email = models.CharField(unique=True, max_length=45)

    def __str__(self):
        return self.name
    

class Car(models.Model):
    car_id = models.AutoField(primary_key=True, )
    car_name = models.CharField(max_length=45)
    price = models.IntegerField()
    color = models.CharField(max_length=10)
    reg_num = models.CharField(max_length=13)
    km_driven = models.IntegerField()
    seats = models.IntegerField()
    fuel_type = models.CharField(max_length=10)
    purc_date = models.DateField()
    no_of_owner = models.IntegerField()
    transmission = models.CharField(max_length=30)
    model_id = models.ForeignKey('Model', models.DO_NOTHING)
    company_id = models.ForeignKey('Company',null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.car_name
    

class CarParts(models.Model):
    car_parts_id = models.AutoField(primary_key=True, )
    part_name = models.CharField(max_length=45)
    price = models.IntegerField()
    car_request_id = models.ForeignKey('CarRequest', null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.part_name
    

class Image(models.Model):
    image_id = models.AutoField(primary_key=True, )
    image_path = models.ImageField(upload_to='images/')
    car_id = models.ForeignKey(Car, null=True, on_delete=models.SET_NULL)



class User(models.Model):
    user_id = models.AutoField(primary_key=True, )
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    email = models.CharField(max_length=45, unique=True)
    password = models.CharField(max_length=20)
    phone = models.CharField(max_length=10)
    area_pincode = models.ForeignKey(Area, null=True, on_delete=models.SET_NULL, db_column='area_area_pincode')
    company_id = models.ForeignKey(Company, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.first_name + ' ' + self.last_name
    

CAR_REQUEST_STATUS = (
    ('pending', 'PENDING'),
    ('accepted', 'ACCEPTED'),
    ('cancel', 'CANCEL'),
)

class CarRequest(models.Model):
    car_request_id = models.AutoField(primary_key=True, )
    car_name = models.CharField(max_length=45)
    car_price = models.IntegerField()
    # token_amt = models.IntegerField()
    fuel_type = models.CharField(max_length=20)
    status = models.CharField(max_length=10, choices=CAR_REQUEST_STATUS, default='PENDING')
    color = models.CharField(max_length=10)
    km_driven = models.IntegerField()
    model_name = models.CharField(max_length=45)
    transmmision = models.CharField(max_length=30)
    # img = models.ImageField(upload_to='images/', default='images/ferari.jpg')
    user_id = models.ForeignKey('User', null=True, on_delete=models.SET_NULL)


    def __str__(self):
        return self.car_name
    

class Inquiry(models.Model):
    inquiry_id = models.AutoField(primary_key=True, )
    inq_text = models.TextField(max_length=300)
    date_time = models.DateTimeField(auto_now_add=True)
    user_id = models.ForeignKey('User', null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.inq_text
    

class CompanyPurchase(models.Model):
    car_request_id = models.ForeignKey(CarRequest, null=True, on_delete=models.SET_NULL)
    user_id = models.ForeignKey('User', null=True, on_delete=models.SET_NULL)
    purc_date = models.DateField()

    def __str__(self):
        return self.car_request_id   


class CompanySell(models.Model):
    car_sell_id = models.AutoField(primary_key=True, )
    sell_date = models.DateField()
    user_id = models.ForeignKey('User', null=True, on_delete=models.SET_NULL)
    car_id = models.ForeignKey(Car, null=True, on_delete=models.SET_NULL)
    com_id = models.ForeignKey('Company', null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.car_id
    


class Complain(models.Model):
    comp_id = models.AutoField(primary_key=True, )
    text = models.TextField(max_length=300)
    date_time = models.DateTimeField(auto_now_add=True)
    user_id = models.ForeignKey('User', null=True, on_delete=models.SET_NULL)
    car_id = models.ForeignKey(Car, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.text
    

class Feedback(models.Model):
    feedback_id = models.AutoField(primary_key=True, )
    feedback_text = models.TextField(max_length=300)
    date_time = models.DateTimeField(auto_now_add=True)
    car_id = models.ForeignKey(Car, null=True, on_delete=models.SET_NULL)
    user_id = models.ForeignKey('User', null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.feedback_text
    

class Payment(models.Model):
    pay_id = models.AutoField(primary_key=True, )
    amount = models.IntegerField()
    date_time = models.DateTimeField(auto_now_add=True)
    user_id = models.ForeignKey('User', null=True, on_delete=models.SET_NULL)
    car_id = models.ForeignKey(Car, null=True, on_delete=models.SET_NULL)



