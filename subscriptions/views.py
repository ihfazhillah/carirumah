import hashlib
from django.shortcuts import render
from django.views.decorators.http import require_POST
from django.core import mail
from .forms import SubscriptionForm

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



