from django.db import models

# Model for New Orders


class NewOrderModel(models.Model):
    # Costumer Details
    first_name = models.CharField(max_length=200, unique=False)
    last_name = models.CharField(max_length=200, unique=False)
    phone_number = models.CharField(max_length=200, unique=False)
    email = models.CharField(max_length=200, unique=True)
    quantity = models.IntegerField(unique=False)

    # Order dates
    date = models.DateTimeField(auto_now_add=False, auto_now=False, blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.first_name
