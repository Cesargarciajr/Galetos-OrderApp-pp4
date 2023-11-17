from django.contrib import admin
from .models import NewOrderModel


@admin.register(NewOrderModel)
class PostNewOrder(admin.ModelAdmin):
    list_display = ('created_on', 'date', 'quantity')
    list_filter = ('created_on', 'date')
    search_fields = ('created_on', 'date',
                     'first_name', 'last_name', 'phone_number', 'email')
    actions = ['approve_orders']

    def approve_orders(self, request, queryset):
        queryset.update(status=True)
