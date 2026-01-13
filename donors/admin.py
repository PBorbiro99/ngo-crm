from django.contrib import admin
from .models import Donor, Donation

@admin.register(Donor)
class DonorAdmin(admin.ModelAdmin):
    list_display = ['name', 'donor_type', 'email', 'phone', 'created_at']
    list_filter = ['donor_type', 'created_at']
    search_fields = ['name', 'email', 'tax_id']

@admin.register(Donation)
class DonationAdmin(admin.ModelAdmin):
    list_display = ['donor', 'amount', 'donation_date', 'receipt_number']
    list_filter = ['donation_date', 'payment_method']
    search_fields = ['donor__name', 'receipt_number']