# ecommerce/urls.py

from django.contrib import admin
from django.urls import path, include

from shop.views import home_view, eshop_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', include('shop.url')),
    path('', home_view, name='home'),
    path('eshop/', eshop_view, name='eshop'),
]
