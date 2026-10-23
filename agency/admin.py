from django.contrib import admin

from .models import Client, Lead, Portfolio, Service, SocialLink


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("title", "price", "created_at")
    search_fields = ("title",)


@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ("title", "project_url", "created_at")
    search_fields = ("title",)
    ordering = ("-created_at",)


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ("name", "sort_order", "is_active", "created_at")
    list_filter = ("is_active",)
    search_fields = ("name",)
    ordering = ("sort_order", "name")
    readonly_fields = ("created_at", "updated_at")


@admin.register(SocialLink)
class SocialLinkAdmin(admin.ModelAdmin):
    list_display = ("platform", "url", "sort_order", "is_active")
    list_editable = ("sort_order", "is_active")
    ordering = ("sort_order", "platform")
    readonly_fields = ("created_at", "updated_at")


@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = ("name", "phone", "is_processed", "created_at")
    list_filter = ("is_processed", "created_at")
    search_fields = ("name", "phone", "message")
