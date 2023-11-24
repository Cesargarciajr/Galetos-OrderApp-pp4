import unittest
from django.test import Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import NewOrderModel, ContactFormModel
from .forms import NewOrderForm, ContactForm


# Setting up automated testing
class ModelsTest(unittest.TestCase):
    def setUp(self):
        # Testing allauth by creating or using existing user
        self.user, created = User.objects.get_or_create(
            username='testuser',
            defaults={'password': 'testpassword'}
        )

    # Testing new order form is working
    def test_new_order_model(self):
        new_order = NewOrderModel.objects.create(
            author=self.user,
            first_name='John',
            last_name='Doe',
            phone_number='123456789',
            email='john.doe@example.com',
            quantity=3,
            date='2023-11-24',
            time='12:00:00',
        )
        self.assertEqual(new_order.first_name, 'John')

    # Testing if contact us form is working
    def test_contact_form_model(self):
        contact_form = ContactFormModel.objects.create(
            first_name='Jane',
            last_name='Doe',
            phone_number='987654321',
            email='jane.doe@example.com',
            message='This is a test message.',
        )
        self.assertEqual(contact_form.first_name, 'Jane')


if __name__ == '__main__':
    unittest.main()
