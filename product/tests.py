from django.test import TestCase
from models import Category

# Create your tests here.
class CategoryTestCase(TestCase):
    def test_no_categories(self):
        response = self.client.get('/products/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No categories")

    def test_login(self):
        response = self.client.get('/products/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "login")

    def test_products24(self):
        response = self.client.get('/products/')
        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, "Products24")


class ProductTestCase(TestCase):
    def test_no_products(self):
        response = self.client.get('/products24/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No products")
