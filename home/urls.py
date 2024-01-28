"""
Module for the home app
"""
from django.urls import path
from . import views
urlpatterns = [
	path('get_data/', views.get_data, name='get_data'),
]
