from django.contrib import admin
from django.urls import path
from .views import product_list, product_detail, view_cart, add_to_cart, remove_from_cart, user_login, SignupView

urlpatterns = [
    path('products/', product_list, name='product_list'),
    path('products/<int:product_id>/', product_detail, name='product_detail'),
    path('cart/', view_cart, name='view_cart'),
    path('cart/add/<int:product_id>/', add_to_cart, name='cart_add'),
    path('cart/remove/<int:product_id>/', remove_from_cart, name='cart_remove'),
    path('login/', user_login, name='login'),
    path('signup/', SignupView.as_view(), name='signup'),

]



