# Create your tests here.
# from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
import json

def test_successful_get_request(client):
    url = reverse('get_data')
    response = client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {'text': 'Hello from Django'}

def test_response_format(client):
    url = reverse('get_data')
    response = client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert response.headers['Content-Type'] == 'application/json'
    assert 'text' in response.json()


def test_other_http_methods_not_allowed(client):
    url = reverse('get_data')
    response_post = client.post(url)
    response_put = client.put(url)
    response_delete = client.delete(url)
    
    assert response_post.status_code == status.HTTP_405_METHOD_NOT_ALLOWED
    assert response_put.status_code == status.HTTP_405_METHOD_NOT_ALLOWED
    assert response_delete.status_code == status.HTTP_405_METHOD_NOT_ALLOWED

def test_absence_of_required_parameters(client):
    url = reverse('get_data')
    response = client.get(url)
    
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {'text': 'Hello from Django'}

def test_presence_of_additional_parameters_ignored(client):
    url = reverse('get_data')
    response = client.get(url + '?additional_param=test')
    
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {'text': 'Hello from Django'}


def test_successful_get_request(client):
    url = reverse('get_data')
    response = client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {'text': 'Hello from Django'}

def test_response_format(client):
    url = reverse('get_data')
    response = client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert response.headers['Content-Type'] == 'application/json'
    assert 'text' in response.json()
