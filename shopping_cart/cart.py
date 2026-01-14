from decimal import Decimal
from catalog.models import Product


class Cart:
    """
    Carrello basato su sessione (NON su database).

    - I dati del carrello vengono salvati dentro request.session
    - request.session è una "memoria" associata al browser dell'utente
    - Struttura usata:
      session["cart"] = {
          "1": {"qty": 2, "price": "19.99"},
          "5": {"qty": 1, "price": "49.90"},
      }
    """

    # Chiave usata per salvare/leggere il carrello dalla sessione
    SESSION_KEY = "cart"

    def __init__(self, request):
        # Salvo un riferimento alla sessione dell'utente
        self.session = request.session

        # Provo a leggere il carrello dalla sessione
        cart = self.session.get(self.SESSION_KEY)

        # Se non esiste ancora (primo accesso), lo creo come dizionario vuoto
        if not cart:
            cart = self.session[self.SESSION_KEY] = {}

        # self.cart è il dizionario vero e proprio con i prodotti
        self.cart = cart

    def add(self, product: Product, qty: int = 1, override_qty: bool = False):
        """
        Aggiunge un prodotto al carrello.

        - qty = quantità da aggiungere (default 1)
        - override_qty = se True, imposta la quantità a qty (non somma)
          utile per il tasto "aggiorna quantità"
        """
        product_id = str(product.id)

        # Se il prodotto non è ancora nel carrello, lo inizializzo
        # Nota: salvo il prezzo come stringa perché la sessione deve contenere dati serializzabili (JSON-friendly)
        if product_id not in self.cart:
            self.cart[product_id] = {
                "qty": 0,
                "price": str(product.price),
            }

        # Se override_qty=True sostituisco la quantità, altrimenti la incremento
        if override_qty:
            self.cart[product_id]["qty"] = qty
        else:
            self.cart[product_id]["qty"] += qty

        self.save()

    def remove(self, product: Product):
        """Rimuove completamente un prodotto dal carrello."""
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def save(self):
        # Dice a Django: "la sessione è cambiata, salvala".
        # Senza modified=True, in alcuni casi Django potrebbe non persistere le modifiche.
        self.session.modified = True

    def __iter__(self):
        """
        Permette di ciclare sul carrello con: for item in cart

        Qui aggiungiamo a ogni item anche l'oggetto Product completo (letto dal DB),
        così nel template possiamo usare item["product"].name, item["product"].image, ecc.
        """
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)

        # Lavoriamo su una copia per aggiungere info senza sporcare il dizionario originale
        cart_copy = self.cart.copy()

        # Aggancio l'oggetto Product a ogni elemento del carrello
        for product in products:
            cart_copy[str(product.id)]["product"] = product

        # Converto price in Decimal e calcolo il totale riga (price * qty)
        for item in cart_copy.values():
            item["price"] = Decimal(item["price"])
            item["total_price"] = item["price"] * item["qty"]
            yield item

    def __len__(self):
        """Numero totale di articoli nel carrello (somma delle quantità)."""
        return sum(item["qty"] for item in self.cart.values())

    def get_total_price(self):
        """Totale complessivo del carrello (somma di price * qty per ogni riga)."""
        return sum(
            Decimal(item["price"]) * item["qty"]
            for item in self.cart.values()
        )

    def clear(self):
        """Svuota il carrello eliminandolo dalla sessione."""
        self.session.pop(self.SESSION_KEY, None)
        self.save()
