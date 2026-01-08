from django.shortcuts import get_object_or_404, redirect, render
from catalog.models import Product
from .cart import Cart


def cart_detail(request):
    cart = Cart(request)
    return render(request, "shopping_cart/cart_detail.html", {"cart": cart})


def cart_add(request, product_id: int):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id, available=True)
    cart.add(product=product)
    return redirect("shopping_cart:cart_detail")


def cart_remove(request, product_id: int):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect("shopping_cart:cart_detail")

def cart_update(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)

    if request.method == "POST":
        qty = int(request.POST.get("qty", 1))
        cart.add(product, qty=qty, override_qty=True)

    return redirect("shopping_cart:cart_detail")
