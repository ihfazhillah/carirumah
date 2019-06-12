from django.urls import path
from .views import register, activate, deactivate


urlpatterns = [
    path('register', register, name='subscription-register'),
    path('activate', activate, name='subscription-activate'),
    path('<int:subscription_id>/deactivate', deactivate, name='subscription-deactivate'),
]
