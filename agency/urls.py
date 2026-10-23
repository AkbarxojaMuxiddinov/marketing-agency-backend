from django.urls import path

from .views import (
    ClientListView,
    LeadCreateView,
    PortfolioListView,
    ServiceListView,
    SocialLinkListView,
)

urlpatterns = [
    path("services/", ServiceListView.as_view(), name="service-list"),
    path("portfolio/", PortfolioListView.as_view(), name="portfolio-list"),
    path("clients/", ClientListView.as_view(), name="client-list"),
    path("social-links/", SocialLinkListView.as_view(), name="social-link-list"),
    path("leads/create/", LeadCreateView.as_view(), name="lead-create"),
]
