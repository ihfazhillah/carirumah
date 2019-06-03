from django import forms
from .models import Subscription


class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscription
        fields = ('email', 'query')


class SubscriptionActivationForm(forms.Form):
    email = forms.EmailField(required=True)
    token = forms.CharField(max_length=255, required=True)
