from django.contrib import admin
from .models import Product

#backend pronto di Django

# Registriamo il modello Product nel pannello Django Admin.
# In questo modo possiamo gestire i prodotti (CRUD) senza creare pagine di backoffice a mano.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    # list_display definisce le colonne visibili nella lista prodotti dell'admin
    list_display = ("name", "price", "available", "updated_at")

    # list_filter aggiunge un filtro laterale (qui: disponibili sì/no)
    list_filter = ("available",)

    # search_fields abilita la ricerca per nome (barra di ricerca in alto)
    search_fields = ("name",)
