from django.db import models
from django.conf import settings

from catalog.models import Product


# Order = "testata" dell'ordine.
# Qui salviamo i dati del cliente e le info generali (data, pagato, utente).
# Un ordine può contenere più prodotti: per quello esiste OrderItem.
class Order(models.Model):
    # Dati cliente (come richiesto dalla traccia)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100, blank=True)  # opzionale
    email = models.EmailField()
    address = models.CharField(max_length=250)

    # Collegamento opzionale all'utente autenticato.
    # Se l'utente è loggato, l'ordine viene associato al suo account.
    # on_delete=SET_NULL: se l'utente viene cancellato, l'ordine resta ma user diventa NULL.
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="orders",
    )

    # Timestamp automatici
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Flag semplice per simulare lo stato pagamento (anche se non hai un vero gateway)
    paid = models.BooleanField(default=False)

    class Meta:
        # Ordini più recenti prima
        ordering = ["-created_at"]

    def __str__(self):
        # Stringa mostrata in Django Admin e in debug
        return f"Order #{self.id}"

    def get_total_cost(self):
        # Somma il costo di tutte le righe (OrderItem) collegate a questo ordine
        # self.items è il related_name definito in OrderItem.order
        return sum(item.get_cost() for item in self.items.all())


# OrderItem = "riga" dell'ordine.
# Ogni riga rappresenta un prodotto acquistato con la sua quantità e prezzo al momento dell'ordine.
class OrderItem(models.Model):
    # Collegamento alla testata dell'ordine (1 ordine -> N righe)
    # CASCADE: se elimino l'ordine, elimino automaticamente anche le sue righe.
    order = models.ForeignKey(
        Order, related_name="items", on_delete=models.CASCADE
    )

    # Prodotto acquistato.
    # PROTECT: impedisce di cancellare un prodotto se è già presente in ordini (buona pratica).
    product = models.ForeignKey(
        Product, related_name="order_items", on_delete=models.PROTECT
    )

    # Prezzo salvato "snapshottato" al momento dell'acquisto (non dipende da future modifiche del Product.price)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    # Quantità acquistata (PositiveIntegerField evita numeri negativi)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)

    def get_cost(self):
        # Totale riga = prezzo * quantità
        return self.price * self.quantity
