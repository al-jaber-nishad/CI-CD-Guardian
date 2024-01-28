from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from django.urls import reverse
import json

class RegisterLoginTests(APITestCase):

    def setUp(self):
        self.register_url = reverse('register')
        self.login_url = reverse('user_login')

    def test_successful_registration_and_login(self):
        registration_data = {'username': 'testuser', 'password': 'testpassword', 'email': 'testuser@example.com'}
        response = self.client.post(self.register_url, registration_data, format='json')

        # Assert that registration was successful
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['message'], 'Registration successful')

        login_data = {'username': 'testuser', 'password': 'testpassword'}
        response = self.client.post(self.login_url, login_data, format='json')

        # Assert that login was successful
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['message'], 'Login successful')

    def test_failed_registration_invalid_data(self):
        invalid_registration_data = {'username': '', 'password': '', 'email': ''}
        response = self.client.post(self.register_url, invalid_registration_data, format='json')

        # Assert that registration failed due to invalid data
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_failed_registration_existing_username(self):
        existing_user = User.objects.create_user(username='existinguser', password='existingpassword', email='existinguser@example.com')
        duplicate_registration_data = {'username': 'existinguser', 'password': 'newpassword', 'email': 'newuser@example.com'}
        response = self.client.post(self.register_url, duplicate_registration_data, format='json')

        # Assert that registration failed due to existing username
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['error'], 'Username is already taken')

    def test_failed_login_invalid_credentials(self):
        invalid_login_data = {'username': 'nonexistentuser', 'password': 'invalidpassword'}
        response = self.client.post(self.login_url, invalid_login_data, format='json')

        # Assert that login failed due to invalid credentials
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response.data['error'], 'Invalid credentials')
