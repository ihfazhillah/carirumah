import pytest
from django.test import Client
from subscriptions.models import Subscription
from django.core import mail


@pytest.mark.django_db
def test_email_subscription_register():
    """testing register subscription"""
    client = Client()
    #1 register subscription
    data = {
        'email': 'test@oke.com',
        'query': 'rumah oke'
    }
    response = client.post('/subscription/register', data)

    assert response.status_code == 200

    #2 check email
    assert len(mail.outbox) == 1

    #3 check db
    subscriptions = Subscription.objects.all()
    assert len(subscriptions) == 1

    #4 check the is_active False
    subscription_data = subscriptions[0]
    assert subscription_data.email == 'test@oke.com'
    assert subscription_data.query == 'rumah oke'
    assert not subscription_data.is_active
