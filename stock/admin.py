from django.contrib import admin

# Register your models here.

from .models import Stock, Company, Inaunit, Warehouse, Stock2, Project


class StockAdmin(admin.ModelAdmin):
    list_display = ('id', 'stock_serial', 'stock_name', 'stock_intime', 'stock_addtime')


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('comp_id', 'comp_name', 'comp_spon')


class InaunitAdmin(admin.ModelAdmin):
    list_display = ('ina_id', 'ina_shortname', 'ina_name')


class WarehouseAdmin(admin.ModelAdmin):
    list_display = ('house_id', 'house_name')


class Stock2Admin(admin.ModelAdmin):
    list_display = ('stock_sn', 'stock_item', 'stock_change', 'stock_time')


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('proj_id', 'proj_name', 'proj_status', 'proj_owner')


admin.site.register(Stock, StockAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Inaunit, InaunitAdmin)
admin.site.register(Warehouse, WarehouseAdmin)
admin.site.register(Stock2, Stock2Admin)
admin.site.register(Project, ProjectAdmin)
