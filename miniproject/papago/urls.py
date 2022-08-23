from django.urls import path, include
from . import views


urlpatterns=[
    path('',views.home, name='home'),
    path('packages',views.packages, name='packages'),
    path('booking',views.booking, name='booking'),
    path('registerUser',views.registerUser,name='registerUser'),
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('loginUser',views.loginUser,name='loginUser'),
    path('payment',views.payment,name='payment'),
    path('traveller',views.traveller,name='traveller'),
    path('logout',views.logout,name='logout'),
    path('addPayment',views.addPayment,name='addPayment'),
    path('create',views.create,name='create'),
    
    
    
]