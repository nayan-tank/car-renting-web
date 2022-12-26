from django.urls import path
from . import views as shopviews
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('login/', shopviews.user_login, name='login'),
    path('logout/', shopviews.user_logout, name='logout'),
    path('signup/', shopviews.user_signup, name='signup'),      
    path('complain/', shopviews.complain, name='complain'),
    path('review/', shopviews.review, name='review'),
    # path('inquiry/', shopviews.inquiry, name='inquiry'),
    path('sellcar/', shopviews.car_request, name='request'),
    path('singlecar/<int:id>', shopviews.cardetails, name='singlecar'),
    path('payment/', shopviews.payment, name='payment'),
    path('dashboard/', shopviews.dashboard, name='dashboard'),
    path('forgotpass/', shopviews.forgotpass, name='forgotpass'),

] +  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# add a flag for
# handling the 404 error
# handler404 = 'first.views.error_404_view'
