"""
Module for the home app
"""
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
	path('get_data/', views.get_data, name='get_data'),
]
