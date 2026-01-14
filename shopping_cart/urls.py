from django.urls import path
from . import views

# Namespace dell'app: serve per riferirsi alle URL nei template in modo sicuro.
# Esempi:
# - {% url 'shopping_cart:cart_detail' %}
# - {% url 'shopping_cart:cart_add' product.id %}
app_name = "shopping_cart"

# URL del carrello:
# - "" = /cart/ (pagina carrello)
# - add/<id>/ = aggiunge un prodotto
# - remove/<id>/ = rimuove un prodotto
# - update/<id>/ = aggiorna quantità (di solito via POST)
urlpatterns = [
    path("", views.cart_detail, name="cart_detail"),
    path("add/<int:product_id>/", views.cart_add, name="cart_add"),
    path("remove/<int:product_id>/", views.cart_remove, name="cart_remove"),
    path("update/<int:product_id>/", views.cart_update, name="cart_update"),
]
