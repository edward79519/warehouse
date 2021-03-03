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
]

