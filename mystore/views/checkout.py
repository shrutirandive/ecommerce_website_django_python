from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from django.views import View

from mystore.models.customer import Customer
from mystore.models.product import Product
from mystore.models.orders import Order
from mystore.middlewares.auth import auth_middleware


class CheckOut(View):
    def get(self, request):
        return render(request, 'checkout.html')

    def post(self, request):
        fullname = request.POST.get('fullname')
        email = request.POST.get('email')
        address = request.POST.get('address')
        city = request.POST.get('city')
        pincode = request.POST.get('pincode')
        phone = request.POST.get('phone')
        customer = request.session.get('customer')
        cart = request.session.get('cart')
        products = Product.get_products_by_id(list(cart.keys()))
        print(address, phone, customer, cart, products)

        for product in products:
            print(cart.get(str(product.id)))
            order = Order(customer=Customer(id=customer),
                          product=product,
                          price=product.price,
                          fullname=fullname,
                          email=email,
                          city=city,
                          pincode=pincode,
                          address=address,
                          phone=phone,
                          quantity=cart.get(str(product.id)))
            order.save()
        request.session['checkout'] = {}

        return redirect('orders')
