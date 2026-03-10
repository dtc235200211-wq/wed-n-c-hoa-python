from django.test import TestCase
from .models import Product


class ProductTest(TestCase):

    def test_create_product(self):

        product = Product.objects.create(
            name="Test",
            sku="SKU001",
            quantity=10,
            price=100
        )

        self.assertEqual(product.name, "Test")