from django import forms
from .models import NewOrderModel, ContactFormModel
from django.utils import timezone


# Render calendar widget
class DateInput(forms.DateInput):
    input_type = 'date'


# Render time selection widget
class TimeInput(forms.TimeInput):
    input_type = 'time'


# Custom form field for phone number with numeric validation
class NumericPhoneNumberField(forms.CharField):
    def validate(self, value):
        super().validate(value)
        try:
            int(value)  # Try converting the value to an integer
        except ValueError:
            raise forms.ValidationError("It must contain only numbers. Ex. 0123456789")


# Defining what will be rendered in the form from NewOrderModel in models.py
class NewOrderForm(forms.ModelForm):

    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    phone_number = NumericPhoneNumberField(required=True)
    email = forms.EmailField(required=True)
    quantity = forms.IntegerField(required=True)


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

    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    phone_number = NumericPhoneNumberField(required=True)
    email = forms.EmailField(required=True)
    message = forms.CharField(required=True)


    class Meta:
        model = ContactFormModel
        fields = ('first_name', 'last_name', 'phone_number',
                  'email', 'message',)
