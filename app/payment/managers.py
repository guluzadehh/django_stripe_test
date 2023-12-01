from django.db.models import Manager
from django.db.models.query import QuerySet


class OrderManager(Manager):
    def get_queryset(self) -> QuerySet:
        return super().get_queryset().prefetch_related("items")
