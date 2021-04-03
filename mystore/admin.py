from django.contrib import admin
from .models.customer import Customer
from .models.category import Category
from .models.product import Product
from .models.orders import Order

#will display in table in djangoAdmin
class AdminCustomer(admin.ModelAdmin):
    list_display=['username', 'phone', 'id']
class AdminCategory(admin.ModelAdmin):
    list_display=['name']
class AdminProduct(admin.ModelAdmin):
    list_display=['name', 'id', 'price', 'category']
class AdminOrder(admin.ModelAdmin):
    list_display=['customer','product','city','status', 'id']

# Register your models here.
admin.site.register(Customer, AdminCustomer)
admin.site.register(Category, AdminCategory)
admin.site.register(Product, AdminProduct)
admin.site.register(Order, AdminOrder)