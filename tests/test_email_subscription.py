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

    # check template
    assert b'We emailed you about subscription\'s activation' in response.content


@pytest.mark.django_db
def test_email_subscription_activation():
    """testing register subscription activation"""
    #1. create dummy data
    subscription = Subscription.objects.create(
        email='test@oke.com',
        query='rumah oke',
        token='helloworld'
    )

    #2. activate through view
    client = Client()
    response = client.get('/subscription/activate?token=helloworld&email=test@oke.com')
    assert response.status_code == 200
    #3. check template
    assert b'Subscription Activated' in response.content
    #4. check database
    subscription = Subscription.objects.filter(
        token='helloworld', query='rumah oke', email='test@oke.com'
    ).first()

    assert subscription is not None
    assert subscription.is_active

