from django.db import models

# Create your models here.

class Stock(models.Model):
    stock_id = models.IntegerField()
    stock_serial = models.CharField(max_length=20)
    stock_name = models.CharField(max_length=30)
    stock_specmain = models.CharField(max_length=30)
    stock_specsub = models.CharField(max_length=30)
    stock_cnts = models.IntegerField()
    stock_totalcnt = models.IntegerField()
    stock_price = models.IntegerField()
    stock_totalprice = models.IntegerField()
    stock_intime = models.DateField()
    stock_outtime =models.DateField()
    stock_comp = models.CharField(max_length=30)
    stock_compcatgo = models.CharField(max_length=20, default="none")
    stock_warehouse = models.CharField(max_length=30)
    stock_project = models.CharField(max_length=10)
    stock_sign = models.CharField(max_length=10)
    stock_addtime = models.DateTimeField(auto_now_add=True)
    stock_updatetime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.stock_serial + self.stock_name
