from django.db import models


# Questo modello rappresenta un "prodotto" del catalogo.
# In pratica: ogni Product = una riga nella tabella del database (SQLite).
# Django userà questi campi per creare la tabella tramite le migrazioni.
class Product(models.Model):
    # Nome del prodotto (campo breve, max 150 caratteri)
    name = models.CharField(max_length=150)

    # Descrizione lunga (blank=True significa: nel form può essere lasciata vuota)
    description = models.TextField(blank=True)

    # Prezzo: Decimal è migliore di float per i soldi (evita errori di arrotondamento)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    # Immagine opzionale del prodotto.
    # upload_to="products/" significa: quando carichi dal form/admin, il file finisce in media/products/
    image = models.ImageField(upload_to="products/", blank=True, null=True)

    # Interruttore per "pubblicare o nascondere" un prodotto senza cancellarlo dal DB.
    # Le pagine del sito filtrano available=True per mostrare solo prodotti disponibili.
    available = models.BooleanField(default=True)

    # Date gestite automaticamente da Django:
    # created_at si imposta SOLO alla creazione, updated_at si aggiorna ad ogni modifica.
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        # Ordinamento di default: quando fai Product.objects.all() li ottieni già ordinati per nome.
        ordering = ["name"]

    def __str__(self) -> str:
        # Questo serve per vedere “T-Shirt” invece di “Product object (1)” nell’admin
        return self.name
