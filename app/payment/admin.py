from django.contrib import admin
from .models import Item, Order, Discount


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display: list[str] = ["name", "price"]
    list_editable: list[str] = ["price"]


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display: list[str] = ["id"]


@admin.register(Discount)
class DiscountAdmin(admin.ModelAdmin):
    list_display: list[str] = ["percent_off"]
