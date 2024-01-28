from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth.models import User

class IntegrationTests(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.register_url = reverse('register')
        self.login_url = reverse('user_login')
        self.show_all_users_url = reverse('show_all_users')

    def test_integration_successful_registration_login_show_all_users(self):
        # Register a user
        registration_data = {'username': 'integrationuser', 'password': 'integrationpassword', 'email': 'integrationuser@example.com'}
        response = self.client.post(self.register_url, registration_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Login with the registered user
        login_data = {'username': 'integrationuser', 'password': 'integrationpassword'}
        response = self.client.post(self.login_url, login_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Access the show_all_users endpoint
        response = self.client.get(self.show_all_users_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['users']), 1)

    def test_integration_failed_login_show_all_users_unauthenticated(self):
        # Access the show_all_users endpoint without authentication
        response = self.client.get(self.show_all_users_url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
