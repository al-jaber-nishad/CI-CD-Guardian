"""
Apps module for the home application.
"""
from django.apps import AppConfig

class HomeConfig(AppConfig):
    """
    Defines the home app config.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'home'
