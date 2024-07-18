# ecommerce/urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import settings, static
from django.contrib.auth.views import LoginView

from shop.views import home_view, eshop_view, view_cart

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', include('shop.url')),
    path('', home_view, name='home'),
    path('eshop/', eshop_view, name='eshop'),
    path('cart/', view_cart, name='cart_view'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)