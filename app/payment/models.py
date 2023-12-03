from django.db import models
from django.urls import reverse
from django.core.validators import MaxValueValidator
from .managers import OrderManager
from .utils import make_line_item


class Item(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self) -> str:
        return reverse("payment:item-detail", kwargs={"pk": self.pk})


class Discount(models.Model):
    percent_off = models.PositiveSmallIntegerField(validators=[MaxValueValidator(99)])

    def __str__(self) -> str:
        return str(self.percent_off)


class Order(models.Model):
    items = models.ManyToManyField(Item, related_name="items")
    discount = models.ForeignKey(Discount, on_delete=models.SET_NULL, null=True)

    objects = OrderManager()

    def make_line_items(self) -> list[dict]:
        return list(map(make_line_item, self.items.all()))

    @property
    def price(self):
        return sum(item.price for item in self.items.all())

    @property
    def clear_price(self):
        return self.price - self.price * self.discount.percent_off / 100
