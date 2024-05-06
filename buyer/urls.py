from django.urls import path
from .views import *


urlpatterns = [
    
    path('register/', register_view, name='register_view'),
    path('otp-verification/', new_otp_verification, name='new_otp_verification'),
    path('login/', login_view, name='login_view'),
    path('forgot_password/', forgot_password, name='forgot_password'),
     path('reset_password/', reset_password, name='reset_password'),
    path('logout/', logout, name='logout'),
    path('', index_view, name='index_view'),
    path('contact/', contact_view, name="contact_view"),
    path('profile/', profile_view, name='profile_view'),
    path('profile-update/', update_info, name='update_info'),
    path('cart/', cart_view, name='cart_view'),
    path('cart/<str:pro_id>/', add_item, name='add_item'),
     path('shopping/', shopping_view, name='shopping_view'),
    
  
]