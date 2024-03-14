from django.test import TestCase
from rest_framework.test import APIRequestFactory
from .views import ProductViewSet
from .models import Product

class ProductAPITestCase(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = ProductViewSet.as_view({'get': 'list'})
        self.product1 = Product.objects.create(name='Product 1', description='Description 1', price=10.0, category='Category 1')
        self.product2 = Product.objects.create(name='Product 2', description='Description 2', price=20.0, category='Category 2')

    def test_list_products(self):
        request = self.factory.get('/products/')
        response = self.view(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)

    def test_search_products(self):
        request = self.factory.get('/products/?search=Product 1')
        response = self.view(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], 'Product 1')

    def test_sort_products_by_name(self):
        request = self.factory.get('/products/?ordering=name')
        response = self.view(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]['name'], 'Product 1')
        self.assertEqual(response.data[1]['name'], 'Product 2')

    def test_sort_products_by_price(self):
        request = self.factory.get('/products/?ordering=price')
        response = self.view(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(float(response.data[0]['price']), 10.0)
        self.assertEqual(float(response.data[1]['price']), 20.0)

    def test_sort_products_by_category(self):
        request = self.factory.get('/products/?ordering=category')
        response = self.view(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]['category'], 'Category 1')
        self.assertEqual(response.data[1]['category'], 'Category 2')

    def test_sort_products_by_description(self):
        request = self.factory.get('/products/?ordering=description')
        response = self.view(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]['description'], 'Description 1')
        self.assertEqual(response.data[1]['description'], 'Description 2')

    def test_sort_products_by_price(self):
        request = self.factory.get('/products/?ordering=price')
        response = self.view(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(float(response.data[0]['price']), 10.0)
        self.assertEqual(float(response.data[1]['price']), 20.0)
