from django.shortcuts import render, redirect
from .forms import OrderCreateForm
from .models import OrderItem
from shopping_cart.cart import Cart


def order_create(request):
    cart = Cart(request)

    if len(cart) == 0:
        return redirect("shopping_cart:cart_detail")

    if request.method == "POST":
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()

            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product=item["product"],
                    price=item["price"],
                    quantity=item["qty"],
                )

            cart.clear()

            return render(request, "orders/order_created.html", {"order": order})
    else:
        form = OrderCreateForm()

    return render(request, "orders/order_create.html", {"cart": cart, "form": form})
