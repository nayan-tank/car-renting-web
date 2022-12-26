from .models import *
from django import forms
from django.contrib.auth.models import User as AuthUser
# from django.contrib.auth.forms import UserCreationForm


# Brand
class BrandModel(forms.ModelForm):
    class Meta:
        model = Brand
        fields = '__all__'


# Model
class CarModel(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'


# Car
class CarModel(forms.ModelForm):
    class Meta:
        model = Model
        fields = '__all__'


# Car Parts
class CarPartModel(forms.ModelForm):
    class Meta:
        model = CarParts
        fields = '__all__'

# City
class CityModel(forms.ModelForm):
    class Meta:
        model = City
        fields = '__all__'


# User
class UserModel(forms.ModelForm):
    class Meta:
        model = AuthUser
        fields = '__all__'