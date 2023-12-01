import stripe
from django.conf import settings
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, TemplateView
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Item, Order
from .utils import make_line_item

stripe.api_key = settings.STRIPE_SECRET_KEY


class StripeSessionIdGenericAPIView(APIView):
    def get(self, request, *args, **kwargs):
        if kwargs["type"] == "order":
            order = get_object_or_404(Order, id=kwargs["pk"])
            line_items = order.make_line_items()
            meta_data = {"order_id": order.id}
            coupon = stripe.Coupon.create(
                percent_off=order.discount.percent_off,
            )
            discounts = [{"coupon": coupon.id}]
        else:
            item = get_object_or_404(Item, id=kwargs["pk"])
            line_items = [make_line_item(item)]
            meta_data = {"item_id": item.id}
            discounts = []

        checkout_session = stripe.checkout.Session.create(
            payment_method_types=["card"],
            line_items=line_items,
            discounts=discounts,
            metadata=meta_data,
            mode="payment",
            success_url=settings.PAYMENT_SUCCESS_URL,
            cancel_url=settings.PAYMENT_CANCEL_URL,
        )

        return Response({"stripe_session_id": checkout_session.id})


class SuccessView(TemplateView):
    template_name = "payment/success.html"


class CancelView(TemplateView):
    template_name = "payment/cancel.html"


class ItemDetailView(DetailView):
    model = Item
    context_object_name = "item"


class OrderDetailView(DetailView):
    model = Order
    queryset = Order.objects.all()
    context_object_name = "order"
