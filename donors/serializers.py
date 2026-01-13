from rest_framework import serializers
from .models import Donor, Donation

class DonorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Donor
        fields = '__all__'

class DonationSerializer(serializers.ModelSerializer):
    donor_name = serializers.CharField(source='donor.name', read_only=True)
    
    class Meta:
        model = Donation
        fields = '__all__'