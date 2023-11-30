from django.urls import path
from .views import ItemDetailView, SuccessView, CancelView

app_name = "payment"

urlpatterns = [
    path("payment/cancel/", CancelView.as_view(), name="cancel"),
    path("payment/success", SuccessView.as_view(), name="success"),
]
