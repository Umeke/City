from django.test import TestCase

# Create your tests here.

#### Step 7: Create Tests




from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Product, Photo, City


class ProductListViewTests(APITestCase):
    def setUp(self):
        self.city1 = City.objects.create(name='City 1')
        self.city2 = City.objects.create(name='City 2')

        self.product1 = Product.objects.create(name='Product 1')
        self.product2 = Product.objects.create(name='Product 2')

        self.photo1 = Photo.objects.create(product=self.product1, image='product_photos/photo1.jpg')
        self.photo2 = Photo.objects.create(product=self.product1, image='product_photos/photo2.jpg', city=self.city1)
        self.photo3 = Photo.objects.create(product=self.product2, image='product_photos/photo3.jpg')

    def test_get_products_without_city(self):
        response = self.client.get(reverse('product-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(len(response.data[0]['photos']), 1)
        self.assertEqual(response.data[0]['photos'][0]['image'], 'product_photos/photo1.jpg')

    def test_get_products_with_city(self):
        response = self.client.get(reverse('product-list'), HTTP_CITY_ID=self.city1.id)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(len(response.data[0]['photos']), 1)
        self.assertEqual(response.data[0]['photos'][0]['image'], 'product_photos/photo2.jpg')
