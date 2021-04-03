from django.db import  models
from django.db.models import Count, Sum

class Category(models.Model):
    name = models.CharField(max_length=50)

    @staticmethod
    def get_all_categories():
        return Category.objects.all()
    

    def __str__(self):
        return self.name
