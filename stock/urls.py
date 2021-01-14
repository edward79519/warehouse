from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="Index"),
    path("add/", views.stock_add, name="AddStock"),
    path('<int:stock_id>/update/', views.stock_update, name="UpdateStock"),
    path('<int:stock_id>/delete/', views.stock_delete, name="DeleteStock"),
]