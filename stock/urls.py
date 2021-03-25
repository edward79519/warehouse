from django.urls import path
from . import views

urlpatterns = [
    path('company/', views.comp, name='Comp_list'),
    path('company/add/', views.companyadd, name='Company_add'),
    path('company/<int:comp_id>/add/', views.companyupdate, name='Company_update'),
    path('inaunit/', views.inaunit, name='Ina_list'),
    path('inaunit/<int:ina_id>/update/', views.inaunitupdate, name='Ina_update'),
    path('project/', views.project, name='Project_list'),
    path('project/add/', views.projectadd, name='Project_add'),
    path('project/<int:project_id>/update/', views.projectupdate, name='Project_update'),
    path('warehouse/', views.warehouse, name='Warehouse_list'),
    path('warehouse/<int:house_id>/update/', views.warehouseupdate, name='Warehouse_update'),
    path('', views.stock, name='Stock_list'),
    path("add/", views.stockadd, name="Stock_add"),
    path("<int:stock_id>/update/", views.stockupdate, name="Stock_update"),
    path('item/', views.item, name='Item_list'),
    path('item/list_del/', views.item_list_del, name='Item_list_del'),
    path('item/add/', views.itemadd, name='Item_add'),
    path('item/<int:item_id>/update/', views.itemupdate, name='Item_update'),
    path('item/<int:item_id>/delete/', views.itemdelete, name='Item_delete'),
    path('category/', views.cate, name='Cate_list'),
    path('category/<int:cate_id>/update/', views.cateupdate, name='Cate_update'),
    path('inout/', views.stockv3, name='Stockv3_list'),
    path('inout/add/', views.stockv3add, name='Stockv3_add'),
    path('inout/<int:stock_id>/update/', views.stockv3update, name='Stockv3_update'),
    path('inout/<int:stock_id>/confirm/', views.stockv3confirm, name='Stockv3_confirm'),
    path('inout/<int:stock_id>/delete/', views.stockv3del, name='Stockv3_delete'),
]

