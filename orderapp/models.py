from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "Pending"), (1, "Approved"))


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="order_post")
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    excerpt = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return self.title


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
    date = models.DateTimeField(auto_now_add=False, auto_now=False, blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.first_name
