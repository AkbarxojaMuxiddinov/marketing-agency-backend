from rest_framework import serializers

from .models import Client, Lead, Portfolio, Service, SocialLink


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ["id", "title", "description", "price"]


class PortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Portfolio
        fields = ["id", "title", "image", "project_url", "created_at"]


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ["id", "name", "logo", "website"]


class SocialLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialLink
        fields = ["id", "platform", "url"]


class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = ["id", "name", "phone", "message", "created_at"]
        read_only_fields = ["id", "created_at", "is_processed"]
