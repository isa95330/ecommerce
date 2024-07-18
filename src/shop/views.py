from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest
from .models import Product, Category

def home_view(request):
    # Votre logique de vue ici
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
            # Gérer le cas où category_id n'est pas un entier valide
            pass

    return render(request, 'product_list.html', {'products': products})

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'product_detail.html', {'product': product})