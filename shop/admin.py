from django.contrib import admin
from .models import *
# from django.contrib.auth.models import User

# Register your models here.

# Company
@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    # list_display = [field.name for field in Company._meta.get_fields()]
    list_display = ['company_id', 'name', 'address', 'contact', 'email']
    search_fields = ('name',)


# Area
@admin.register(Area)
class AreaAdmin(admin.ModelAdmin):
    # list_display = [field.name for field in Area._meta.get_fields()]
    list_display = ['area_pincode', 'area_name', 'city_id' ]
    list_editable = ('area_name',)
    search_fields = ('area_name',)
    

# City
@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    # list_display = [field.name for field in City._meta.get_fields()]
    list_display = ['city_id', 'city_name']
    list_editable = ('city_name',)
    search_fields = ('city_name',)


# Brand
@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    # list_display = [field.name for field in Brand._meta.get_fields()]
    list_display = ['brand_id', 'brand_name']
    search_fields = ('brand_name',)


# Model
@admin.register(Model)
class ModelAdmin(admin.ModelAdmin):
    # list_display = [field.name for field in Model._meta.get_fields()]
    list_display = ['model_id', 'model_name', 'year', 'engine', 'description', 'brand_id']
    search_fields = ('model_name',)
    list_per_page = 10
    list_filter = ('brand_id', )


# Car
@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    # list_display = [field.name for field in Car._meta.get_fields()]
    list_display = [ 'car_id', 'car_name', 'price', 'color', 'reg_num', 'km_driven', 'seats', 'fuel_type', 'purc_date', 'no_of_owner', 'transmission', 'img', 'model_id' ]
    search_fields = ('car_name', 'color', 'price', 'fuel_type', 'transmission')
    list_per_page = 10
    list_filter = ('model_id',  'color', 'transmission',)


# Company sell
@admin.register(CompanySell)
class CompanySellAdmin(admin.ModelAdmin):
    # list_display = [field.name for field in CompanySell._meta.get_fields()]
    list_display = [ 'sell_id', 'sell_date', 'user_id', 'car_id' ]
    search_fields = ('sell_date',)


# Company purchase
@admin.register(CompanyPurchase)
class CompanyPurchaseAdmin(admin.ModelAdmin):
    # list_display = [field.name for field in CompanyPurchase._meta.get_fields()]
    list_display = [ 'req_id', 'user_id', 'purc_date' ]
    search_fields = ('purc_date',)


# Image
@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    # list_display = [field.name for field in Image._meta.get_fields()]
    list_display = ['image_id', 'image_path', 'car_id']
    search_fields = ('car_id',)


# Car request
@admin.register(CarRequest)
class CarRequestAdmin(admin.ModelAdmin):
    # list_display = [field.name for field in CarRequest._meta.get_fields()]
    list_display = [ 'car_request_id', 'car_name', 'car_price', 'fuel_type', 'status', 'color', 'km_driven', 'model_name', 'transmission', 'image', 'user_id' ]
    search_fields = ('car_name', 'color', 'car_price', 'fuel_type', 'model_name', 'transmission')
    list_per_page = 10
    list_filter = ('model_name', 'color', 'transmission', )


# Car parts
@admin.register(CarParts)
class CarPartsAdmin(admin.ModelAdmin):
    list_display = ['car_parts_id', 'part_name', 'price', 'car_request_id']
    search_fields = ('part_name',)
    list_filter = ('car_request_id', )


# Inquiry
@admin.register(Inquiry)
class InquiryAdmin(admin.ModelAdmin):
    # list_display = [field.name for field in Inquiry._meta.get_fields()]
    list_display = [ 'inquiry_id', 'email', 'inq_text', 'date_time', 'user_id' ]
    search_fields = ('email', 'inq_text')


# Payment
@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = [ 'pay_id', 'amount', 'date_time', 'user_id', 'car_id' ]
    search_fields = ('amount', )


# Complain
@admin.register(Complain)
class ComplainAdmin(admin.ModelAdmin):
    list_display = ['complain_id', 'subject', 'complain_text', 'date_time', 'user_id' ]
    search_fields = ('subject',)


# Review
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = [ 'review_id', 'review_text', 'date_time', 'user_id' ]
    search_fields = ('review_text', )