from django.contrib import admin
from django.urls import path
from .views import product_list, product_detail, view_cart, add_to_cart, remove_from_cart, SignupView, \
    MyTokenObtainPairView, MyTokenRefreshView, UserLoginView, ClientListView, MyTokenVerifyView, LoginView

urlpatterns = [
    path('products/', product_list, name='product_list'),
    path('products/<int:product_id>/', product_detail, name='product_detail'),
    path('cart/', view_cart, name='view_cart'),
    path('cart/add/<int:product_id>/', add_to_cart, name='cart_add'),
    path('cart/remove/<int:product_id>/', remove_from_cart, name='cart_remove'),
    # API JWT
    # URL pour obtenir le token JWT
    path('api/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    # URL pour rafraîchir un token d'accès expiré en utilisant le token de rafraîchissement.
    path('api/token/refresh/', MyTokenRefreshView.as_view(), name='token_refresh'),
    # Vérifie la validité d'un token JWT. Elle permet de confirmer si le token est encore valide et non expiré.
    path('api/token/verify/', MyTokenVerifyView.as_view(), name='token_verify'),
    # Gère la connexion des utilisateurs en validant leurs identifiants. Si les identifiants sont corrects,
    # elle génère un JWT et le retourne à l'utilisateur.
    path('api/login/', UserLoginView.as_view(), name='api_user_login'),

    # Vues traditionnelles
    path('login/', LoginView.as_view(), name='login'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('clients/', ClientListView.as_view(), name='client_list'),

]



