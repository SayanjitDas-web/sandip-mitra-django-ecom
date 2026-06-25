from django.urls import path
from . import views

urlpatterns = [
    path(
        "create/<int:product_id>/",
        views.create_order,
        name="create_order"
    ),
    path(
        "my-orders/",
        views.my_orders,
        name="my_orders"
    ),
    path(
        "<int:id>/",
        views.order_detail,
        name="order_detail"
    ),
    path(
        "cancel/<int:id>/",
        views.cancel_order,
        name="cancel_order"
    ),
]
