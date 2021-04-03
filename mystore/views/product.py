from django.shortcuts import render,redirect, HttpResponseRedirect
from mystore.models.customer import Customer
from mystore.models.product import Product as pd
from mystore.models.category import Category
from django.views import View

class Product(View):

    def post(self , request):
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity<=1:
                        cart.pop(product)
                    else:
                        cart[product]  = quantity-1
                else:
                    cart[product]  = quantity+1

            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1

        request.session['cart'] = cart
        print('cart' , request.session['cart'])
        return redirect('product')



    def get(self , request):
        return HttpResponseRedirect(f'/mystore{request.get_full_path()[1:]}')


def mystore(request):
    cart = request.session.get('cart')
    if not cart:
        request.session['cart'] = {}
    products = None
    categories = Category.get_all_categories()
    categoryID = request.GET.get('category')
    if categoryID:
        products = pd.get_all_products_by_categoryid(categoryID)
    else:
        products = pd.get_all_products()
    data = {'products':products, 'categories':categories}
    print('you are : ', request.session.get('username'))
    return render(request, 'product.html', data)
