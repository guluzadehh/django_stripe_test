from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)


class Order(models.Model):
    items = models.ManyToManyField(Item, related_name="items")

    def make_line_items(self):
        def callback(item):
            return {
                "price_data": {
                    "currency": "rub",
                    "unit_amount_decimal": item.price * 100,
                    "product_data": {
                        "name": item.name,
                        "description": item.description,
                    },
                },
                "quantity": 1,
            }

        return list(map(callback, self.items))

    @property
    def price(self):
        return sum(item.price for item in self.items)
