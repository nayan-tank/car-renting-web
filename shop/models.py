from django.db import models
import datetime
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django import forms
from .helpers import *

# import uuid

# Admin
# class Admin(models.Model):
#     # admin_id = models.UUIDField(auto_created=True)
#     first_name = models.CharField(max_length=20)
#     last_name = models.CharField(max_length=20)
#     phone = models.CharField(max_length=10)
#     email = models.CharField(unique=True, max_length=30)
#     password = models.CharField(max_length=20)
#     area = models.CharField(max_length=50, null=True)
#     # area_pincode = models.ForeignKey('Area', null=True, on_delete=models.SET_NULL, db_column='area_area_pincode')

#     def __str__(self):
#         return self.first_name + ' ' + self.last_name


# User
# class User(models.Model):
#     user_id = models.AutoField(primary_key=True,)
#     first_name = models.CharField(max_length=10)
#     last_name = models.CharField(max_length=10)
#     email = models.CharField(max_length=45, unique=True)
#     password = models.CharField(max_length=20)
#     phone = models.CharField(max_length=10)
#     area_pincode = models.ForeignKey(Area, null=True, on_delete=models.SET_NULL, db_column='area_area_pincode')
#     company_id = models.ForeignKey(Company, null=True, on_delete=models.SET_NULL)

#     def __str__(self):
#         return self.first_name + ' ' + self.last_name


# User Profile
# class UserProfile(models.Model):
#     user   = models.OneToOneField(User, null=True ,on_delete=models.SET_NULL)
#     avatar = models.ImageField(upload_to='avatar/', default='avatar/default.png')


# City
class City(models.Model):
    city_id = models.AutoField(primary_key=True, )
    city_name = models.CharField(max_length=20, unique=True, validators=[clean_city_name])

    def __str__(self):
        return self.city_name

    
# Area
class Area(models.Model):
    area_pincode = models.CharField(primary_key=True, max_length=6, unique=True, validators=[clean_area_pincode])
    area_name = models.CharField(max_length=45, validators=[clean_area_name])
    city_id = models.ForeignKey('City', null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.area_name

# Brand
class Brand(models.Model):
    brand_id = models.AutoField(primary_key=True,)
    brand_name = models.CharField(max_length=45, unique=True, validators=[clean_brand_name])

    def __str__(self):
        return self.brand_name


# Model
class Model(models.Model):
    model_id = models.AutoField(primary_key=True, )
    model_name = models.CharField(max_length=45, unique=True)
    year = models.CharField(max_length=4, default=datetime.datetime.now().strftime('%Y'))
    engine = models.CharField(max_length=30)
    # car_stock = models.IntegerField(default=1)
    description = models.CharField(max_length=200)
    brand_id = models.ForeignKey(Brand, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.model_name 
    

# Company
class Company(models.Model):
    company_id = models.AutoField(primary_key=True, )
    name = models.CharField(max_length=45)
    address = models.CharField(max_length=45)
    contact = models.CharField(max_length=10, validators=[clean_contact])
    email = models.CharField(unique=True, max_length=45)

    def __str__(self):
        return self.name
    
    

# Car Sold Status
CAR_SOLD_STATUS = (
    (0, 0),
    (1, 1)
)


# Car
class Car(models.Model):
    car_id = models.AutoField(primary_key=True, )
    car_name = models.CharField(max_length=45)
    price = models.IntegerField()
    color = models.CharField(max_length=10, validators=[clean_color])
    reg_num = models.CharField(max_length=13, validators=[clean_regno])
    km_driven = models.IntegerField()
    seats = models.IntegerField()
    fuel_type = models.CharField(max_length=10, validators=[clean_fuel_type])
    purc_date = models.DateField()
    no_of_owner = models.IntegerField()
    transmission = models.CharField(max_length=30, validators=[clean_transmission])
    sold_out = models.IntegerField(choices=CAR_SOLD_STATUS, default=0)
    img = models.ImageField(upload_to='images/', default='images/car1.jpg')
    model_id = models.ForeignKey('Model', models.DO_NOTHING)
    company_id = models.ForeignKey('Company',null=True, on_delete=models.SET_NULL, default=1)

    def __str__(self):
        return self.car_name
    
    class Meta:
        ordering = ['car_id']


# Image
class Image(models.Model):
    image_id = models.AutoField(primary_key=True, )
    image_path = models.ImageField(upload_to='images/')
    car_id = models.ForeignKey(Car, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.car_id


# Car Parts
class CarParts(models.Model):
    car_parts_id = models.AutoField(primary_key=True, )
    part_name = models.CharField(max_length=45, validators=[clean_car_parts])
    price = models.IntegerField()
    car_request_id = models.ForeignKey('CarRequest', null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.part_name


# CAR REQUEST STATUS 
CAR_REQUEST_STATUS = (
    ('Pending', 'PENDING'),
    ('Accepted', 'ACCEPTED'),
    ('Cancel', 'CANCEL'),
)

# Fuel Types
# FUEL_TYPES = (
#     ('Petrol', 'PETROL'),
#     ('Disel', 'DISEL'),
#     ('Gas', 'GAS'),
# )


# Car Request
class CarRequest(models.Model):
    car_request_id = models.AutoField(primary_key=True, )
    car_name = models.CharField(max_length=45, validators=[clean_car_name])
    car_price = models.IntegerField()
    # token_amt = models.IntegerField()
    fuel_type = models.CharField(max_length=20, validators=[clean_fuel_type])
    status = models.CharField(max_length=10, choices=CAR_REQUEST_STATUS, default='Pending')
    color = models.CharField(max_length=10, validators=[clean_color])
    km_driven = models.IntegerField()
    model_name = models.CharField(max_length=45, validators=[clean_model_name])
    transmission = models.CharField(max_length=30, validators=[clean_transmission])
    image = models.ImageField(upload_to='req_car_img/', max_length=300,)
    user_id = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)


    def __str__(self):
        return self.car_name


# Inquiry
class Inquiry(models.Model):
    inquiry_id = models.AutoField(primary_key=True, )
    email = models.EmailField(max_length=300,)
    inq_text = models.TextField(max_length=300, validators=[clean_inq_text])
    date_time = models.DateTimeField(auto_now_add=True)
    user_id = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.inq_text


# Comapany Purchase
class CompanyPurchase(models.Model):
    req_id = models.ForeignKey(CarRequest, null=True, on_delete=models.SET_NULL)
    user_id = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    purc_date = models.DateField()

    def __str__(self):
        return self.car_request_id   


# Company Sell
class CompanySell(models.Model):
    sell_id = models.AutoField(primary_key=True, )
    sell_date = models.DateField()
    user_id = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    car_id = models.ForeignKey(Car, null=True, on_delete=models.SET_NULL)
    company_id = models.ForeignKey('Company', null=True, on_delete=models.SET_NULL, default=1)

    def __str__(self):
        return str(self.car_id)


# Complain
class Complain(models.Model):
    complain_id = models.AutoField(primary_key=True)
    subject = models.CharField(max_length=50, validators=[clean_complain_sub])
    complain_text = models.TextField(max_length=300, validators=[clean_complain_text])
    date_time = models.DateTimeField(auto_now_add=True)
    user_id = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    # car_id = models.ForeignKey(Car, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.text
    

# Review
class Review(models.Model):
    review_id = models.AutoField(primary_key=True, )
    review_text = models.TextField(max_length=300, validators=[clean_review_text])
    date_time = models.DateTimeField(auto_now_add=True)
    # car_id = models.ForeignKey(Car, null=True, on_delete=models.SET_NULL)
    user_id = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.review_text
    

# Payment
class Payment(models.Model):
    pay_id = models.AutoField(primary_key=True, )
    amount = models.IntegerField()
    date_time = models.DateTimeField(auto_now_add=True)
    user_id = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    car_id = models.ForeignKey(Car, null=True, on_delete=models.SET_NULL)



