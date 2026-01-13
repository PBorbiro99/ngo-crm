from django.db import models

class Donor(models.Model):
    DONOR_TYPE = [
        ('individual', 'Individual'),
        ('company', 'Company'),
        ('foundation', 'Foundation'),
    ]
    
    name = models.CharField(max_length=200)
    donor_type = models.CharField(max_length=20, choices=DONOR_TYPE)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.TextField(blank=True)
    tax_id = models.CharField(max_length=50, blank=True)  # CIF/CNP for Romanian law
    created_at = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(blank=True)
    
    def __str__(self):
        return self.name

class Donation(models.Model):
    donor = models.ForeignKey(Donor, on_delete=models.CASCADE, related_name='donations')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    donation_date = models.DateField()
    payment_method = models.CharField(max_length=50)
    purpose = models.CharField(max_length=200, blank=True)
    receipt_number = models.CharField(max_length=50, unique=True)
    notes = models.TextField(blank=True)
    
    def __str__(self):
        return f"{self.donor.name} - {self.amount} RON"