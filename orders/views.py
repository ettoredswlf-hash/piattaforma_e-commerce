from django.shortcuts import render, redirect
from .forms import OrderCreateForm
from .models import OrderItem
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
            # Salvo la "testata" ordine nel DB (Order)
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
