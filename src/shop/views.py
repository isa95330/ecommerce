from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpRequest
from django.views import View
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from .models import Product, Category, CartItem, Client

# Vue pour l'obtention du token JWT
class UserLoginView(View):
    def post(self, request):
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                refresh = RefreshToken.for_user(user)
                return Response({
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                }, status=status.HTTP_200_OK)
        return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

def home_view(request):
    return render(request, 'home.html')

def eshop_view(request):
    categories = Category.objects.all()
    return render(request, 'eshop.html', {'categories': categories})

def product_list(request: HttpRequest):
    category_id = request.GET.get('category')
    products = Product.objects.all()

    if category_id:
        try:
            category_id = int(category_id)  # Assurez-vous que category_id est un entier valide
            products = products.filter(category_id=category_id)
        except ValueError:
            pass

    return render(request, 'product_list.html', {'products': products})

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'product_detail.html', {'product': product})

@login_required
def view_cart(request):
    cart = request.session.get('cart', {})
    products = []
    for product_id, quantity in cart.items():
        product = get_object_or_404(Product, id=product_id)
        products.append({'product': product, 'quantity': quantity})
    return render(request, 'cart.html', {'products': products})

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart = request.session.get('cart', {})
    if product_id in cart:
        cart[product_id] += 1
    else:
        cart[product_id] = 1
    request.session['cart'] = cart
    return redirect('view_cart')

@login_required
def remove_from_cart(request, product_id):
    cart = request.session.get('cart', {})
    if product_id in cart:
        del cart[product_id]
    request.session['cart'] = cart
    return redirect('view_cart')

class LoginView(View):
    def get(self, request):
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})

    def post(self, request):
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect('home')
        return render(request, 'login.html', {'form': form})

class ClientListView(View):
    def get(self, request):
        clients = Client.objects.all()
        return render(request, 'client_list.html', {'clients': clients})

class SignupView(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, 'signup.html', {'form': form})

    def post(self, request):
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
            login(request, user)
            return redirect('home')
        return render(request, 'signup.html', {'form': form})

# Pour obtenir un nouveau token
class MyTokenObtainPairView(TokenObtainPairView):
    pass

# Pour rafraîchir un token
class MyTokenRefreshView(TokenRefreshView):
    pass

# Pour vérifier un token
class MyTokenVerifyView(TokenVerifyView):
    pass
