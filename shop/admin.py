from django.contrib import admin
from .models import *

# Register your models here.

models = [Admin, Area, City, Brand, Model, User, Company, CompanyPurchase, CompanySell, Car, CarParts, CarRequest, Image, Inquiry, Payment]

admin.site.register(models)

@admin.register(Complain)
class ComplainAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Complain._meta.get_fields()]

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Feedback._meta.get_fields()]

