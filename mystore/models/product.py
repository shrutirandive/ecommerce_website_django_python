from django.db import models
from django.db.models import Count, Sum
from .category import Category

class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description = models.CharField(max_length=200, default='' , null=True , blank=True)
    image = models.ImageField(upload_to='uploads/products/')

    #display exact Product instead of Product object(1)
    def __str__(self):
        return self.name

    @staticmethod
    #function will retrieve all data from Products and can be used to display on screen(html)
    def get_all_products():
        return Product.objects.all()

    @staticmethod
    def get_no_of_products_byCategory():
        return Product.objects.values('category_id').annotate(mycount = Count('category_id'))
        #return Product.objects.values(category=category_id)
      
    @staticmethod
    def get_products_by_id(ids):
        return Product.objects.filter(id__in =ids)


    @staticmethod
    def get_all_products_by_categoryid(category_id):
        if category_id:
            return Product.objects.filter(category = category_id)
        else:
            return Product.get_all_products()
