from django.contrib import admin
from django.urls import path
from .views import getCountry

urlpatterns = [
    path('', getCountry, name="getCountry"),
]