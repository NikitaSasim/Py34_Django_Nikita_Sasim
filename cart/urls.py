from django.contrib import admin
from django.urls import path
from .views import CartView, CartViewRemove


urlpatterns = [
    path('add/', CartView.as_view(), name="cart-add"),
    path('remove/', CartViewRemove.as_view(), name="cart-remove")
]
