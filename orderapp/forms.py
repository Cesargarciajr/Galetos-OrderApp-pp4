from django import forms
from .models import NewOrderModel, ContactFormModel
from django.utils import timezone


# Render calendar widget
class DateInput(forms.DateInput):
    input_type = 'date'

# Render time selection widget
class TimeInput(forms.TimeInput):
    input_type = 'time'


# Defining what will be rendered in the form from NewOrderModel in models.py
class NewOrderForm(forms.ModelForm):

    class Meta:
        model = NewOrderModel
        fields = ('first_name', 'last_name', 'phone_number',
                  'email', 'quantity', 'date', 'time',)
        widgets = {
            'date': DateInput(attrs={'type': 'date', 'min': timezone.now().strftime('%Y-%m-%d')}),
            'time': TimeInput(),
        }


# Defining what will be rendered in the form from ContactFormModel in models.py
class ContactForm(forms.ModelForm):

    class Meta:
        model = ContactFormModel
        fields = ('first_name', 'last_name', 'phone_number',
                  'email', 'message',)
