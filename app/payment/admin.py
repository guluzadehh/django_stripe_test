from django.contrib import admin
from .models import Item


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display: list[str] = ["name", "price"]
    list_editable: list[str] = ["price"]
