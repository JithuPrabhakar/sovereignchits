from django.contrib import admin
from .models import Scheme


@admin.register(Scheme)
class SchemeAdmin(admin.ModelAdmin):
    list_display = ['name', 'sala', 'instalments', 'period', 'coming_soon', 'is_active', 'created_at']
    list_filter = ['coming_soon', 'is_active', 'created_at']
    search_fields = ['name', 'period']
    list_editable = ['is_active', 'coming_soon']
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'is_active', 'coming_soon')
        }),
        ('Scheme Details', {
            'fields': ('sala', 'instalments', 'instalment_amount', 'period', 'auction_bid', 'auction_date')
        }),
        ('Display', {
            'fields': ('header_color',),
            'description': 'Use CSS classes like "gradient-primary", "bg-gradient-to-r from-blue-500 to-blue-700", etc.'
        }),
    )
    
    def save_model(self, request, obj, form, change):
        # Auto-set coming_soon if key fields are missing
        if not obj.instalments or not obj.auction_bid:
            obj.coming_soon = True
        super().save_model(request, obj, form, change)
