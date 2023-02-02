from django.contrib import admin
from django.urls import path
from .views import CartView


urlpatterns = [
    path('add/', CartView.as_view(), name="cart-add")
]
