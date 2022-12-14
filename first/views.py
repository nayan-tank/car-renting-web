
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def error_404_view(request, exception):
    return render(request, '_404.html')