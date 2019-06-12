import hashlib
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseNotFound
from django.views.decorators.http import require_POST
from django.core import mail
from .forms import SubscriptionForm, SubscriptionActivationForm
from .models import Subscription

# Create your views here.


def register(request):
    form = SubscriptionForm(request.POST)

    if form.is_valid():
        subscription = form.save(commit=False)

        # process token
        token = hashlib.sha256(f'{subscription.email}{subscription.query}{subscription.created_at}'.encode()).hexdigest()
        subscription.token = token

        subscription.save()

        mail.send_mail(
            'Subscription Activation',
            (
                'Please activate your subscription by click on this link:'
                f'{subscription.token}'
            ),
            'Carirumah <mihfazhillah@gmail.com>',
            [subscription.email]
        )

        return render(
            request,
            'subscription/register-done.html'
        )
    return render(
        request,
        'subscription/register-failed.html',
        {'errors': form.errors}
    )


def activate(request):
    form = SubscriptionActivationForm(request.GET, request.POST)
    if form.is_valid():

        subscription = get_object_or_404(
            Subscription,
            token=form.cleaned_data.get('token'),
            email=form.cleaned_data.get('email')
        )
        subscription.is_active = True
        subscription.save()

        return render(
            request,
            'subscription/activate-done.html'
        )
    return render(
        request,
        'subscription/activate-failed.html',
        {'errors': form.errors}
    )


def deactivate(request, subscription_id):
    subscription = get_object_or_404(Subscription, id=subscription_id)
    subscription.is_active = False
    subscription.save()

    return render(
        request,
        'subscription/deactivate-done.html'
    )
