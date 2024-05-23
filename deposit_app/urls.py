from django.contrib import admin
from django.urls import path, include
from .views import index, deposit, welcome

urlpatterns = [
    path("", welcome, name="welcome"),
    path("index", index, name="index"),
    path("deposit", deposit, name="deposit"),
]
