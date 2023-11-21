from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "Pending"), (1, "Approved"))


class NewOrderModel(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="new_order")
    # Costumer Details
    first_name = models.CharField(max_length=200, unique=False)
    last_name = models.CharField(max_length=200, unique=False)
    phone_number = models.CharField(max_length=200, unique=False)
    email = models.CharField(max_length=200, unique=True)
    quantity = models.IntegerField(unique=False)

    # Order dates
    date = models.DateField()
    time = models.Field()
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.first_name


class ContactFormModel(models.Model):
    first_name = models.CharField(max_length=200, unique=False)
    last_name = models.CharField(max_length=200, unique=False)
    phone_number = models.CharField(max_length=200, unique=False)
    email = models.CharField(max_length=200, unique=True)
    message = models.TextField(max_length=500, unique=False)

    def __str__(self):
        return self.first_name
