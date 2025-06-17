from django.contrib import admin
from .models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'tracking_code', 'sender', 'recipient', 'status', 'weight_kg',
        'declared_value', 'created_at', 'updated_at'
    )
    search_fields = ('tracking_code', 'sender', 'recipient')
    list_filter = ('status', 'created_at')
    readonly_fields = ('created_at', 'updated_at')
    ordering = ('-created_at',)
