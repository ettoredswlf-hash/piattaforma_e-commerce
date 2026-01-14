from django.shortcuts import get_object_or_404, redirect, render
from catalog.models import Product
from .cart import Cart


# Pagina principale del carrello.
# Qui  leggiamo il contenuto del carrello (in sessione)
# e lo mostriamo tramite un template.
def cart_detail(request):
    cart = Cart(request)
    return render(request, "shopping_cart/cart_detail.html", {"cart": cart})


# Azione "Add to cart":
# - prende il prodotto dal database (se esiste e se available=True)
# - lo aggiunge al carrello salvato in sessione
# - fa redirect alla pagina /cart/ per vedere il risultato
def cart_add(request, product_id: int):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id, available=True)
    cart.add(product=product)
    return redirect("shopping_cart:cart_detail")


# Azione "Remove":
# - rimuove completamente un prodotto dal carrello
# - poi redirect alla pagina carrello
def cart_remove(request, product_id: int):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect("shopping_cart:cart_detail")


# Azione "Update quantity":
# - arriva da un form (POST) che invia la nuova qty
# - override_qty=True significa: "imposta la quantità esattamente a qty"
#   (non sommare)
def cart_update(request, product_id: int):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)

    # Usiamo POST per aggiornare dati (buona pratica: le modifiche non si fanno con GET)
    if request.method == "POST":
        qty = int(request.POST.get("qty", 1))
        cart.add(product, qty=qty, override_qty=True)

    return redirect("shopping_cart:cart_detail")
