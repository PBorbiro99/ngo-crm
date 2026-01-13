from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Donor, Donation
from .serializers import DonorSerializer, DonationSerializer

class DonorViewSet(viewsets.ModelViewSet):
    queryset = Donor.objects.all()
    serializer_class = DonorSerializer
    permission_classes = [IsAuthenticated]

class DonationViewSet(viewsets.ModelViewSet):
    queryset = Donation.objects.all()
    serializer_class = DonationSerializer
    permission_classes = [IsAuthenticated]