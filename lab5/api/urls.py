from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.all_products),
    path('products/<id>/', views.id_product),
    path('categories/', views.all_categories),
    path('categories/<id>', views.id_category),
    path('categories/<id>/prodcuts', views.category_products),
]
