from django import forms
from django.forms import DateInput
from .models import NewOrderModel, ContactFormModel


class NewOrderForm(forms.ModelForm):

    class Meta:
        model = NewOrderModel
        fields = ('first_name', 'last_name', 'phone_number',
                  'email', 'quantity', 'date')


class ContactForm(forms.ModelForm):

    class Meta:
        model = ContactFormModel
        fields = ('first_name', 'last_name', 'phone_number',
                  'email', 'message',)