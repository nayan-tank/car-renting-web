from .models import *
from django import forms
from django.core import validators
from django.contrib.auth.models import User as AuthUser
from django.contrib.auth.forms import UserCreationForm


# sing up 
class SignUpForm(UserCreationForm):
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput, required=True)
    phone = forms.CharField(max_length=10, required=True)
    class Meta:
        model = AuthUser
        fields = ['username', 'first_name', 'last_name', 'email']


# complain
class UserComplain(forms.ModelForm):
    class Meta:
        model = Complain
        fields = '__all__'


# feedback
class UserFeedback(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = '__all__'

    
# car request
class UserRequest(forms.ModelForm):
    class Meta:
        model = CarRequest
        fields = '__all__'


# inquiry
class UserInquiry(forms.ModelForm):
    class Meta:
        model = Inquiry
        fields = '__all__'




