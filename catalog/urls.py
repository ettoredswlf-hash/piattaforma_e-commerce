from django.urls import path
from . import views

# app_name serve per creare un "namespace" nelle URL.
# Così nei template puoi scrivere:
# {% url 'catalog:product_detail' product.pk %}
# e Django capisce che deve cercare il name="product_detail" dentro questa app.
app_name = "catalog"

# urlpatterns è la lista delle rotte (URL) gestite da questa app.
# Ogni path collega:
# - una stringa URL
# - una view (funzione Python)
# - un nome (name=...) utile per generare link in modo automatico.
urlpatterns = [
    # Homepage del sito: esegue product_list
    path("", views.product_list, name="product_list"),

    # Pagina dettaglio prodotto:
    # <int:pk> cattura un numero dall'URL e lo passa alla view come parametro pk.
    # Esempio: /products/3/ -> pk=3
    path("products/<int:pk>/", views.product_detail, name="product_detail"),
    
]
