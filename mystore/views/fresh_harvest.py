from django.shortcuts import render,redirect, HttpResponseRedirect
from django.views import View
from mystore.models.customer import Customer

def fresh_harvest(request):
    return render(request, 'fresh_harvest.html', {})
def sidebar(request):
    return render(request, 'sidebar.html', {})
