from django.urls import path
from .views import ItemDetailView, OrderDetailView, SuccessView, CancelView

app_name = "payment"

urlpatterns = [
    path("items/<int:pk>/", ItemDetailView.as_view(), name="item-detail"),
    path("orders/<int:pk>/", OrderDetailView.as_view(), name="order-detail"),
    path("payment/cancel/", CancelView.as_view(), name="cancel"),
    path("payment/success/", SuccessView.as_view(), name="success"),
]
