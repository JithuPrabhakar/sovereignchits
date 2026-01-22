from django.db import models


class Scheme(models.Model):
    """Model for chit fund schemes"""
    name = models.CharField(max_length=200)
    sala = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True, help_text="Sala amount in ₹")
    instalments = models.IntegerField(null=True, blank=True, help_text="Number of instalments")
    auction_bid = models.CharField(max_length=50, null=True, blank=True, help_text="Auction bid percentage or amount")
    period = models.CharField(max_length=50, null=True, blank=True, help_text="Period (e.g., Months, Weeks)")
    instalment_amount = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True, help_text="Instalment amount in ₹")
    auction_date = models.TextField(null=True, blank=True, help_text="Auction date information")
    header_color = models.CharField(max_length=100, default='gradient-primary', help_text="Header color class (e.g., gradient-primary, bg-gradient-to-r from-blue-500 to-blue-700)")
    coming_soon = models.BooleanField(default=False, help_text="Mark as coming soon if scheme details are incomplete")
    is_active = models.BooleanField(default=True, help_text="Show this scheme on the website")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name

    @property
    def is_complete(self):
        """Check if scheme has all required details"""
        return bool(self.sala and self.instalments and self.auction_bid)

