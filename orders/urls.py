from django.urls import path
from . import views

app_name = "orders"

urlpatterns = [
    # Checkout / creazione ordine
    path("create/", views.order_create, name="order_create"),

    # Area utente: i miei ordini
    path("my/", views.order_list, name="order_list"),
    path("my/<int:order_id>/", views.order_detail, name="order_detail"),
]
