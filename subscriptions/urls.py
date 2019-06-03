from django.urls import path
from .views import register, activate


urlpatterns = [
    path('register', register, name='subscription-register'),
    path('activate', activate, name='subscription-activate'),
]
