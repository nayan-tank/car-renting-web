from django.contrib import admin
from .models import *
# from django.contrib.auth.models import User

# Register your models here.

models = [ Area, City, Brand, Model, Company, CompanyPurchase, CompanySell, Car, CarParts, CarRequest, Image, Inquiry, Payment]

admin.site.register(models)

@admin.register(Complain)
class ComplainAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Complain._meta.get_fields()]

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Feedback._meta.get_fields()]

