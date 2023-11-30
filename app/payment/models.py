from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)


class Order(models.Model):
    items = models.ManyToManyField(Item, related_name="items")

    @property
    def price(self):
        return sum(item.price for item in self.items)
