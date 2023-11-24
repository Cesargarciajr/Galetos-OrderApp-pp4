from django.db import models
from django.contrib.auth.models import User

# Defining variable for status of the orders
STATUS = ((0, "Pending"), (1, "Approved"))


# Model that creates all the fields required to create new order
class NewOrderModel(models.Model):
    # Determines the user as author
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="new_order")

    # Costumer and order Details
    first_name = models.CharField(max_length=200, unique=False)
    last_name = models.CharField(max_length=200, unique=False)
    phone_number = models.CharField(max_length=200, unique=False)
    email = models.CharField(max_length=200, unique=False)
    quantity = models.IntegerField(unique=False)

    # Order dates and status
    date = models.DateField(auto_now=False, auto_now_add=False)
    time = models.TimeField(auto_now=False, auto_now_add=False)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.first_name

# Model that defines fields necessary to contact form
class ContactFormModel(models.Model):
    # Costumer details and message
    first_name = models.CharField(max_length=200, unique=False)
    last_name = models.CharField(max_length=200, unique=False)
    phone_number = models.CharField(max_length=200, unique=False)
    email = models.CharField(max_length=200, unique=False)
    message = models.TextField(max_length=500, unique=False)

    def __str__(self):
        return self.first_name
