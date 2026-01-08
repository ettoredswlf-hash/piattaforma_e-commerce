from decimal import Decimal
from catalog.models import Product


class Cart:
    """
    Session-based shopping cart.
    Stored in request.session as a dictionary.
    """

    SESSION_KEY = "cart"

    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(self.SESSION_KEY)
        if not cart:
            cart = self.session[self.SESSION_KEY] = {}
        self.cart = cart

    def add(self, product: Product, qty: int = 1, override_qty: bool = False):
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {
                "qty": 0,
                "price": str(product.price),
            }

        if override_qty:
            self.cart[product_id]["qty"] = qty
        else:
            self.cart[product_id]["qty"] += qty

        self.save()

    def remove(self, product: Product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def save(self):
        self.session.modified = True

    def __iter__(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)

        cart_copy = self.cart.copy()
        for product in products:
            cart_copy[str(product.id)]["product"] = product

        for item in cart_copy.values():
            item["price"] = Decimal(item["price"])
            item["total_price"] = item["price"] * item["qty"]
            yield item

    def __len__(self):
        return sum(item["qty"] for item in self.cart.values())

    def get_total_price(self):
        return sum(
            Decimal(item["price"]) * item["qty"]
            for item in self.cart.values()
        )

    def clear(self):
        """Remove cart from session."""
        self.session.pop(self.SESSION_KEY, None)
        self.save()
  
