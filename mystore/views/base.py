from django.shortcuts import render,redirect, HttpResponseRedirect
from django.views import View
from mystore.models.customer import Customer

# Create your views here.
#class Base(View):
def base(request):
    return render(request, 'base.html', {})
