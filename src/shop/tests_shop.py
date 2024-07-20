from django.test import TestCase
from .models import Product, Category

class ProductTestCase(TestCase):
    def setUp(self):
        # Création d'une catégorie pour associer les produits
        self.category = Category.objects.create(
            name="Test Category",
            description="Test Category Description",
            image="uploads/test_category.jpg"
        )

        # Création des produits associés à la catégorie
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
