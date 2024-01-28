# Create your tests here.
from rest_framework.test import APIClient, APITestCase
from django.contrib.auth.models import User
from rest_framework import status
from django.urls import reverse


class ShowAllUsersTests(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.show_all_users_url = reverse('show_all_users')

    def test_successful_show_all_users_authenticated(self):
        # Log in a user
        user = User.objects.create_user(username='testuser', password='testpassword', email='testuser@example.com')
        self.client.force_authenticate(user=user)

        # Access the show_all_users endpoint
        response = self.client.get(self.show_all_users_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_failed_show_all_users_unauthenticated(self):
        # Access the show_all_users endpoint without authentication
        response = self.client.get(self.show_all_users_url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
