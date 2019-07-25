from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('leads.urls'))  # leads app urls file
]
