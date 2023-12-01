from django.urls import path
from .views import StripeSessionIdGenericAPIView

app_name = "api"

urlpatterns = [
    path(
        "buy/<string:type>/<int:pk>/",
        StripeSessionIdGenericAPIView.as_view(),
        name="buy-item",
    )
]
