from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from django.views import View

from mystore.models.customer import Customer
from mystore.models.product import Product
from mystore.models.orders import Order
from mystore.middlewares.auth import auth_middleware

class OrderView(View):


    def get(self , request ):
        customer = request.session.get('customer')
        orders = Order.get_orders_by_customer(customer)
        print(orders)
        return render(request , 'orders.html'  , {'orders' : orders})