from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.



class UserProfile(AbstractUser,models.Model):
    usermoney = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

class HaveStock(models.Model):
    owner = models.ForeignKey(UserProfile)
    mystock = models.CharField(max_length=50)
    count = models.IntegerField()


class Stock(models.Model):
    StockItem = models.CharField(max_length=30,unique=True)
    StockPrice = models.IntegerField()


class News(models.Model):
    content = models.CharField(max_length=2048)
    variation = models.IntegerField()



#stock = HaveStock.objects.create(owner=UserProfile.objects.get(id=1),mystock='layer7',count=5)
#user = UserProfile.objects.create(username='admin',usermoney=999999999999)
#user.set_password('admina')
#user.save()