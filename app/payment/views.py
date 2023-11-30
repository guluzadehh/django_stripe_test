import stripe
from django.conf import settings
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, TemplateView
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Item

stripe.api_key = settings.STRIPE_SECRET_KEY


class StripeSessionIdGenericAPIView(APIView):
    def get(self, request, *args, **kwargs):
        item = get_object_or_404(Item, id=kwargs["pk"])

        checkout_session = stripe.checkout.Session.create(
            payment_method_types=["card"],
            line_items=[
                {
                    "price_data": {
                        "currency": "rub",
                        "unit_amount_decimal": round(item.price * 100, 1),
                        "product_data": {
                            "name": item.name,
                            "description": item.description,
                        },
                    },
                    "quantity": 1,
                }
            ],
            metadata={"item_id": item.id},
            mode="payment",
            success_url="http://localhost:8000/",
        )

        return Response({"stripe_session_id": checkout_session.id})


class SuccessView(TemplateView):
    template_name = "payment/success.html"


class CancelView(TemplateView):
    template_name = "payment/cancel.html"
