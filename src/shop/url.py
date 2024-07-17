# shop/url.py

from django.urls import path, include

from .views import product_list, product_detail

urlpatterns = [

    path('products/', product_list, name='product_list'),
    path('products/<int:product_id>/', product_detail, name='product_detail'),
]
