from django.db import models
from .product import Product
from .customer import Customer
import datetime

PINCODES= [
    ('400601','400601'),
    ('400602','400602'),
    ('400604','400604'),
    ('400608','400608'),
    ]


class Order(models.Model):

    product = models.ForeignKey(Product,
                                on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer,
                                 on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    fullname = models.CharField(max_length=50,default='')
    email = models.EmailField(max_length=100,default='')
    address = models.CharField(max_length=50, default='', blank=True)
    city = models.CharField(max_length=50, default='', blank=True)
    pincode = models.CharField(max_length=6, choices=PINCODES, default='400601')
    phone = models.CharField(max_length=10, default='', blank=True)
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)

        
    def placeOrder(self):
        self.save()

    @staticmethod
    def get_orders_by_customer(customer_id):
        return Order.objects.filter(customer=customer_id).order_by('-date')

    
