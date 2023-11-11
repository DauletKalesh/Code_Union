from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User

# Create your tests here.

class CurrencyAPITests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='testpass')
        self.token = self.client.post(
            '/api/auth/login/', 
            {'username': 'testuser', 'password': 'testpass'}).json()['token']

    def test_get_currencies_authenticated(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)
        response = self.client.get('/api/currencies/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_currencies_unauthenticated(self):
        response = self.client.get('/api/currencies/')
        self.assertIn(
            response.status_code, 
            (status.HTTP_401_UNAUTHORIZED, status.HTTP_403_FORBIDDEN))
