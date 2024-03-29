from django import forms
from .models import NewOrderModel, ContactFormModel
from django.utils import timezone


# Render calendar widget
class DateInput(forms.DateInput):
    input_type = 'date'


# Render time selection widget
class TimeInput(forms.TimeInput):
    input_type = 'time'


class NumericPhoneNumberField(forms.CharField):
    def validate(self, value):
        super().validate(value)
        if not value.isdigit():  # Check if value contains non-digit characters
            raise forms.ValidationError("It must contain only numbers. Ex. 0123456789")


# Custom form field to get valid number
class PositiveIntegerField(forms.IntegerField):
    def __init__(self, *args, **kwargs):
        kwargs['min_value'] = 1  # Set minimum value to 1
        super().__init__(*args, **kwargs)

    def validate(self, value):
        super().validate(value)
        if value <= 0:
            raise forms.ValidationError("Quantity must be a positive number.")


# Defining what will be rendered in the form from NewOrderModel in models.py
class NewOrderForm(forms.ModelForm):

    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    phone_number = NumericPhoneNumberField(required=True)
    email = forms.EmailField(required=True)
    quantity = PositiveIntegerField(required=True)


    class Meta:
        model = NewOrderModel
        fields = ('first_name', 'last_name', 'phone_number',
                  'email', 'quantity', 'date', 'time',)
        widgets = {
            'date': DateInput(attrs={'type': 'date', 'min': timezone.now().strftime('%Y-%m-%d')}),
            'time': TimeInput(attrs={'type': 'time', 'min': '10:00', 'max': '16:00'}),
        }
        


# Defining what will be rendered in the form from ContactFormModel in models.py
class ContactForm(forms.ModelForm):

    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    phone_number = NumericPhoneNumberField(required=True)
    email = forms.EmailField(required=True)
    message = forms.CharField(required=True)


    class Meta:
        model = ContactFormModel
        fields = ('first_name', 'last_name', 'phone_number',
                  'email', 'message',)
