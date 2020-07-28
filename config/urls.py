"""
django_property_management_api URL Configuration.
The `urlpatterns` list routes URLs to views.
"""
from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls')), # DRF browsable API
    path("properties/", include("properties.urls", namespace="properties")),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns
