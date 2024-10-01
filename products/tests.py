from django.test import TestCase
from .models import Product, Category  # Adjust based on your actual models

class ProductTest(TestCase):
    def test_product_creation(self):
        # Create a category first
        category = Category.objects.create(name="Test Category")  # Adjust based on your model
        
        # Now create a product with the category
        product = Product.objects.create(name="Test Product", price=9.99, category=category)  # Adjust as needed
        
        # Assertions
        self.assertEqual(product.name, "Test Product")
        self.assertEqual(product.price, 9.99)
        self.assertEqual(product.category.name, "Test Category")  # Assuming a category field exists
