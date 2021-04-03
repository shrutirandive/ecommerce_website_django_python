from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from mystore.models.customer import Customer

from django.views import View
import requests
import json

class Signup(View):
    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):
        postData = request.POST
        username = postData.get('username')
        phone = postData.get('phone')
        password = postData.get('password')

        
        # validation
        value = {
            'username': username,
            'phone': phone,

        }
        error_message = None
        #creation of objects
        customer = Customer(username=username,
                            phone=phone,
                            password=password)
        error_message = self.validateCustomer(customer)

        if not error_message:
            print(username, phone, password)
            customer.password = make_password(customer.password)
            customer.register()
            return redirect('login')
        else:
            data = {
                'error': error_message,
                'values': value
            }
            return render(request, 'signup.html', data)

        #ReCaptcha stuff
        captcha_token = request.POST.get('g-recaptcha-response')
        captcha_url="https://www.google.com/recaptcha/api/siteverify"
        captcha_secret = '6Lcb3h4aAAAAAKdKixtq7jxaVkYJWkaBxkpSotno'
        captcha_data={
            'secret':captcha_secret,
            'response':captcha_token
        }
        captcha_server_resposnse=requests.post(url=captcha_url, data=captcha_data)
        captcha_json=json.loads(captcha_server_resposnse.text)
        if captcha_json['success']==True:
            return redirect('login')
        else:        
            error_message(request, "invalid captcha")
            return render(request, 'signup.html', data)
            
    def validateCustomer(self, customer):
        error_message = None
        if (not customer.username):
            error_message = "Username Required !!"
        elif len(customer.username) < 3:
            error_message = 'Username must be 3 char long or more'
        elif not customer.phone:
            error_message = 'Phone Number required'
        elif len(customer.phone) < 10:
            error_message = 'Phone Number must be 10 char Long'


        elif customer.isExists():
            error_message = 'Username Already Registered..'
        # saving

        return error_message
