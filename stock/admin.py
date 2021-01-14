from django.contrib import admin

# Register your models here.

from .models import Stock

class StockAdmin(admin.ModelAdmin):
    list_display = ('id', 'stock_serial', 'stock_name', 'stock_intime', 'stock_addtime')


admin.site.register(Stock, StockAdmin)