from django.contrib import admin
from .models import Cart
# Register your models here.


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['user', 'display_products', 'get_total_price', 'get_total_quantity']
