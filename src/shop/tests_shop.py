# shop/tests_shop.py

from django.test import TestCase, SimpleTestCase
from django.urls import reverse, resolve
from .models import Product, Category
from .views import product_list


class ProductTestCase(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Test Category")
        self.product1 = Product.objects.create(
            category=self.category,
            name="Test Product 1",
            price=10.00,
            description="Test Description 1",
            image="uploads/test1.jpg",
            quantity=5
        )
        self.product2 = Product.objects.create(
            category=self.category,
            name="Test Product 2",
            price=20.00,
            description="Test Description 2",
            image="uploads/test2.jpg",
            quantity=10
        )

    def test_product_retrieval(self):
        products = Product.objects.all()
        self.assertEqual(products.count(), 2)
        self.assertEqual(products[0].name, "Test Product 1")
        self.assertEqual(products[1].name, "Test Product 2")

    def test_product_detail(self):
        product = Product.objects.get(name="Test Product 1")
        self.assertEqual(product.price, 10.00)
        self.assertEqual(product.description, "Test Description 1")
        self.assertEqual(product.quantity, 5)


class TestUrls(SimpleTestCase):
    def test_products_url_resolves(self):
        url = reverse('product_list')
        resolver = resolve(url)
        self.assertEqual(resolver.func, product_list)