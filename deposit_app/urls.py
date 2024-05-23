from django.contrib import admin
from django.urls import path, include
from .views import index, deposit

urlpatterns = [
    path(" ", index, name="index"),
    path("deposit", deposit, name="deposit"),
]
