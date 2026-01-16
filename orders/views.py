from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .forms import OrderCreateForm
from .models import Order, OrderItem
from shopping_cart.cart import Cart


# Crea un ordine a partire dal carrello (sessione).
# Flusso:
# 1) se carrello vuoto -> rimando al carrello
# 2) GET -> mostro form dati cliente
# 3) POST -> valido form, creo Order, creo OrderItem, svuoto carrello, mostro conferma
def order_create(request):
    cart = Cart(request)

    # Se il carrello è vuoto non ha senso creare un ordine
    if len(cart) == 0:
        return redirect("shopping_cart:cart_detail")

    if request.method == "POST":
        # Creo il form con i dati inseriti dall'utente
        form = OrderCreateForm(request.POST)

        # is_valid() controlla i vincoli (email valida, campi obbligatori, lunghezze, ecc.)
        if form.is_valid():
            # Salvo la "testata" ordine nel DB (Order) ma prima voglio attaccarci l'utente se loggato
            order = form.save(commit=False)

            # Se l'utente è autenticato, collego l'ordine al suo account
            # (se non è loggato, user resta NULL e va bene lo stesso)
            if request.user.is_authenticated:
                order.user = request.user

            order.save()

            # Creo le righe ordine (OrderItem) copiando i dati dal carrello
            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product=item["product"],
                    price=item["price"],   # prezzo "fotografato" al momento dell'ordine
                    quantity=item["qty"],
                )

            # Una volta creato l'ordine, svuoto il carrello (checkout completato)
            cart.clear()

            # Pagina di conferma
            return render(request, "orders/order_created.html", {"order": order})
    else:
        # GET: form vuoto da mostrare all'utente
        form = OrderCreateForm()

    # Se GET oppure POST non valido: mostro la pagina con form + carrello
    return render(request, "orders/order_create.html", {"cart": cart, "form": form})


# Lista ordini dell'utente loggato.
# - login_required: se non sei loggato ti rimanda al login
# - filtro per user=request.user: ognuno vede SOLO i suoi ordini
@login_required
def order_list(request):
    orders = Order.objects.filter(user=request.user).order_by("-created_at")

    return render(
        request,
        "orders/order_list.html",
        {"orders": orders},
    )


# Dettaglio di un singolo ordine dell'utente loggato.
# Nota: metto user=request.user nel get_object_or_404 così evito che qualcuno
# provi a vedere un ordine di un altro semplicemente cambiando l'id nell'URL.
@login_required
def order_detail(request, order_id: int):
    order = get_object_or_404(Order, id=order_id, user=request.user)

    # Prendo le righe dell'ordine (OrderItem) collegate
    items = order.items.select_related("product").all()

    return render(
        request,
        "orders/order_detail.html",
        {"order": order, "items": items},
    )
