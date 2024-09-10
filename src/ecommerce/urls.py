# ecommerce/urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import settings, static
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from shop.views import home_view, eshop_view, view_cart

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', include('shop.url')),
    path('', home_view, name='home'),
    path('eshop/', eshop_view, name='eshop'),
    path('cart/', view_cart, name='cart_view'),
    # URL pour obtenir le token JWT
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # URL pour rafraîchir le token JWT
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)