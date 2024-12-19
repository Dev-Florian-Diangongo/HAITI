# superuser_login/urls.py
from django.urls import path
from .views import superuser_login,deconnexion

urlpatterns = [
    path('dashbord/', superuser_login, name='login'),
    path('deconnexion/', deconnexion, name='deconnexion'),
    
      
]




