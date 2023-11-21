from django import forms
from .models import NewOrderModel, ContactFormModel


class DateInput(forms.DateInput):
    input_type = 'date'

class TimeInput(forms.TimeInput):
    input_type = 'time'

class NewOrderForm(forms.ModelForm):

    class Meta:
        model = NewOrderModel
        fields = ('first_name', 'last_name', 'phone_number',
                  'email', 'quantity', 'date', 'time',)
        widgets = {
            'date': DateInput(),
            'time': TimeInput(),
        }


class ContactForm(forms.ModelForm):

    class Meta:
        model = ContactFormModel
        fields = ('first_name', 'last_name', 'phone_number',
                  'email', 'message',)
