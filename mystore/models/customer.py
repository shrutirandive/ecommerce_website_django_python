from django.db import models
from django.core.validators import MinLengthValidator
#from captcha.fields import CaptchaField

# Create your models here.
class Customer(models.Model):
    username=models.CharField(max_length=50)
    phone=models.CharField(max_length=10)
    password=models.CharField(max_length=500)
    
    #display exact username instead of Username object(1)
    def __str__(self):
        return self.username

    def register(self):
        self.save()

    @staticmethod
    def get_customer_by_username(username):
        try:
            return Customer.objects.get(username=username)
        except:
            return False

    def isExists(self):
        if Customer.objects.filter(username=self.username):
            return True

        return False

    