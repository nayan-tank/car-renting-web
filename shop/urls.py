from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('signup/', views.user_signup, name='signup'),
    path('complain/', views.complain, name='complain'),
    path('feedback/', views.feedback, name='feedback'),
    path('inquiry/', views.inquiry, name='inquiry'),
    path('request/', views.car_request, name='request'),
    path('payment/', views.payment, name='payment'),
    path('dashboard/', views.dashboard, name='dashboard'),
]

# add a flag for
# handling the 404 error
handler404 = 'first.views.error_404_view'
