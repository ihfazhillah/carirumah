import pytest
from django.test import Client, RequestFactory
# from landing.views import search, scrape


def test_search_post_context(mocker):
    # mocker.patch('landing.views.scrape')
    client = Client()
    response = client.post('/search', {'query': 'hello'})
    # TODO: work with patch
    # response = search(request)
    # scrape.assert_called_once_with('hello')

    context = response.context

    query = context.get('query')
    assert query == 'hello'
    
    subscription_form = context.get('form')
    assert subscription_form

    subscription_action = context.get('subscription_action')

    assert subscription_action == '/subscription/register'
    

