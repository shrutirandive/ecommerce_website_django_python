from django.contrib import admin
from django.urls import path
from .views.base import base
from .views.fresh_harvest import fresh_harvest, sidebar
from .views.signup import Signup
from .views.login import Login, logout
from .views.product import Product, mystore

from .views.cart import Cart
from .views.checkout import CheckOut
from .views.orders import OrderView

from .middlewares.auth import  auth_middleware
#from django.urls import re_path
urlpatterns = [
    path('fresh', fresh_harvest, name='fresh'),
    path('base', base, name='base'),
    path('signup', Signup.as_view(), name='signup'),
    path('login', Login.as_view(), name='login'),
    path('logout', logout , name='logout'),
    path('', Product.as_view(), name='product'),
    path('mystore', mystore, name='mystore'),
    
    path('cart', auth_middleware(Cart.as_view()) , name='cart'),
    path('checkout', CheckOut.as_view() , name='checkout'),
    path('orders', auth_middleware(OrderView.as_view()), name='orders'),
    

    #path('sidebar', sidebar, name='sidebar'),
    #path('product/?category.id/', mystore, name='mystore'),
]
