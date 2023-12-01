from django.db import models
from .managers import OrderManager
from .utils import make_line_item


class Item(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)


class Order(models.Model):
    items = models.ManyToManyField(Item, related_name="items")

    objects = OrderManager()

    def make_line_items(self) -> list[dict]:
        return list(map(make_line_item, self.items.all()))

    @property
    def price(self):
        return sum(item.price for item in self.items.all())
