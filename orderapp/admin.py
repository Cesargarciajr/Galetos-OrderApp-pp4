from django.contrib import admin
from .models import NewOrderModel, ContactFormModel


@admin.register(NewOrderModel)
class PostNewOrder(admin.ModelAdmin):
    list_display = ('created_on','first_name', 'date', 'quantity', 'status')
    list_filter = ('created_on', 'date', 'quantity', 'status')
    search_fields = ('created_on', 'date',
                     'first_name', 'last_name', 'phone_number', 'email', 'status')
    actions = ['approve_orders']

    def approve_orders(self, request, queryset):
        queryset.update(status=True)

@admin.register(ContactFormModel)
class PostNewMessage(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone_number', 'email')
    list_filter = ('first_name', 'last_name', 'phone_number', 'email')
    search_fields = ('first_name', 'last_name', 'phone_number', 'email')