from django.shortcuts import render , redirect , HttpResponseRedirect
from django.contrib.auth.hashers import  check_password
from mystore.models.customer import Customer
from django.views import  View

class Login(View):
    return_url = None
    def get(self , request):
        Login.return_url = request.GET.get('return_url')
        return render(request , 'login.html')

    def post(self , request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        customer = Customer.get_customer_by_username(username)
        error_message = None
        if customer:
            flag = check_password(password, customer.password)
            if flag:
                request.session['customer'] = customer.id

                if Login.return_url:
                    return HttpResponseRedirect(Login.return_url)
                else:
                    Login.return_url = None
                    return redirect('product')
            else:
                error_message = 'Username or Password invalid !!'
        else:
            error_message = 'Username or Password invalid !!'

        print(username, password)
        return render(request, 'login.html', {'error': error_message})

def logout(request):
    request.session.clear()
    return redirect('login')
