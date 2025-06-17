from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('tracking_code', 'sender', 'recipient',
                    'status', 'created_at', 'updated_at')
    search_fields = ('tracking_code', 'sender', 'recipient')
    list_filter = ('status',)
