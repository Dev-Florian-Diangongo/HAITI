# superuser_login/urls.py
from django.urls import path
from .views import superuser_login

urlpatterns = [
    path('dashbord/', superuser_login, name='superuser_login'),
]
