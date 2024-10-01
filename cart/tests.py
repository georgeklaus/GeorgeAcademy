from django.test import TestCase
from .models import CartItem
from products.models import Product
from django.contrib.auth.models import User

class CartItemTest(TestCase):
    def test_cart_item_creation(self):
        # Create a test user and product
        user = User.objects.create(username='testuser')
        product = Product.objects.create(name='Test Product', price=9.99)  # Adjust according to your Product model
        
        # Create a cart item
        cart_item = CartItem.objects.create(user=user, product=product, quantity=1)

        # Assertions
        self.assertEqual(cart_item.user.username, 'testuser')
        self.assertEqual(cart_item.product.name, 'Test Product')
        self.assertEqual(cart_item.quantity, 1)
