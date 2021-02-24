from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="Index"),
    path("add/", views.stock_add, name="AddStock"),
    path('<int:stock_id>/update/', views.stock_update, name="UpdateStock"),
    path('<int:stock_id>/delete/', views.stock_delete, name="DeleteStock"),
    path('company/', views.comp, name='Comp_list'),
    path('inaunit/', views.inaunit, name='Ina_list'),
    path('project/', views.project, name='Project_list'),
    path('project/add/', views.projectadd, name='Project_add'),
    path('project/<int:project_id>/update/', views.projectupdate, name='Project_update'),
    path('warehouse/', views.warehouse, name='Warehouse_list'),
    path('list/', views.stock, name='Stock_list'),
    path("list/add/", views.stockadd, name="Stock_add"),
]

