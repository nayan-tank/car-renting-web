from django.shortcuts import render
from .forms import *
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from first import urls 
from .models import *


# User Registration 
def user_signup(request):
    if request.method == 'POST':
        fm = SignUpForm(request.POST)
       
        if fm.is_valid():
            fm.save()
            uname = fm.cleaned_data['username']
            password = fm.cleaned_data['password1']
            user = authenticate(username=uname, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
        else:
            print('error')
    else:
        fm = SignUpForm()
    return render(request, 'signup.html', {'fm': fm})


# User Login 
def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            fm = AuthenticationForm(request=request, data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                password = fm.cleaned_data['password']
                user = authenticate(username=uname, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('dashboard')
        else:
            fm = AuthenticationForm()
    else:
        return redirect('dashboard')
    return render(request, 'login.html', {'fm':fm})


def user_logout(request):
    logout(request)
    return redirect('login')


# Dashboard
def dashboard(request):
    if request.user.is_authenticated:
        return render(request, 'profile.html', )
    else:
        return redirect('login')





# User Car Request
def car_request(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            fm = UserRequest(request.POST)
            if fm.is_valid():
                fm.save()
        else:
            fm = UserRequest()
    else:
        return redirect('login')
    return render(request, 'request.html', {'fm': fm})



# Complain 
def complain(request):
    if request.method == 'POST':
        fm = UserComplain(request.POST)
        if fm.is_valid():
            fm.save()
    else:
        fm = UserComplain()
    return render(request, 'complain.html', {'fm': fm})



# Inquiry
def inquiry(request):
    if request.method == 'POST':
        fm = UserInquiry(request.POST)
        if fm.is_valid():
            fm.save()
    else:
        fm = UserInquiry()
    return render(request, 'inquiry.html', {'fm': fm})



# Feedback
def feedback(request):
    if request.method == 'POST':
        fm = UserFeedback(request.POST)
        if fm.is_valid():
            fm.save()
    else:
        fm = UserFeedback()
    return render(request, 'feedback.html', {'fm': fm})



# Payment
def payment(request):
    pass



# Error Page
def error_404_view(request, exception):
    return render(request, '_404.html')

