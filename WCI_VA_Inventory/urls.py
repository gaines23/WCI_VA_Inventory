"""
Definition of urls for Inventory_VA.
"""

from datetime import datetime
from django.urls import path, include
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls, name="admin"),
    path('', include('app.urls'), name="home"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)