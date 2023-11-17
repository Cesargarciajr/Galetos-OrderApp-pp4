from django import forms
from .models import NewOrderModel


class NewOrderForm(forms.ModelForm):

    class Meta:
        model = NewOrderModel
        fields = ('first_name', 'last_name', 'phone_number',
                  'email', 'quantity', 'date')
