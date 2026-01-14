from django.contrib import admin
from .models import Order, OrderItem


# Inline = permette di gestire le righe (OrderItem) direttamente dentro la pagina dell'ordine.
# TabularInline le mostra in formato tabella (più compatto e chiaro).
class OrderItemInline(admin.TabularInline):
    model = OrderItem

    # raw_id_fields evita dropdown enormi se hai tanti prodotti:
    # invece della select, ti fa una casella con ricerca per ID.
    raw_id_fields = ("product",)


# Registriamo Order nell'admin per poter:
# - vedere tutti gli ordini
# - filtrare per pagato/data
# - aprire un ordine e vedere/modificare le righe (OrderItem) inline
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    # Colonne visibili nella lista ordini
    list_display = ("id", "user", "email", "created_at", "paid")

    # Filtri rapidi nella sidebar
    list_filter = ("paid", "created_at")

    # Mostra le righe ordine dentro l'ordine (come "sotto-tabella")
    inlines = [OrderItemInline]
