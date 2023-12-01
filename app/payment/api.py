from django.urls import path
from .views import StripeSessionIdGenericAPIView

app_name = "api"

urlpatterns = [
    path(
        "buy/<str:type>/<int:pk>/",
        StripeSessionIdGenericAPIView.as_view(),
        name="buy-item",
    )
]
