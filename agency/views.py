from django.views.generic import TemplateView
from rest_framework import generics

from .models import Client, Lead, Portfolio, Service, SocialLink
from .serializers import (
    ClientSerializer,
    LeadSerializer,
    PortfolioSerializer,
    ServiceSerializer,
    SocialLinkSerializer,
)


class HomePageView(TemplateView):
    template_name = "agency/home.html"


class ServiceListView(generics.ListCreateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class PortfolioListView(generics.ListCreateAPIView):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer


class ClientListView(generics.ListAPIView):
    queryset = Client.objects.filter(is_active=True)
    serializer_class = ClientSerializer


class SocialLinkListView(generics.ListAPIView):
    queryset = SocialLink.objects.filter(is_active=True)
    serializer_class = SocialLinkSerializer


class LeadCreateView(generics.CreateAPIView):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer
