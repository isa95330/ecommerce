from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='shop', null=True, blank=True)

    class Meta:
        app_label = 'shop'

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    description = models.TextField()
    image = models.ImageField(upload_to='shop', null=True, blank=True)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return self.name