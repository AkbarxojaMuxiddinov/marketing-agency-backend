"""
URL configuration for marketing_agency project.
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from agency.views import HomePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('admin/', admin.site.urls),
    path('api/v1/', include('agency.urls')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
