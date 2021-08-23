from django import forms
from .models import Order


class OrderCreatedForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('last_name', 'first_name', 'phone', 'address')
