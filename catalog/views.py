from django.shortcuts import get_object_or_404, render
from .models import Product


# Questa view gestisce la HOME del sito (lista prodotti).
# Una "view" in Django è una funzione che:
# 1) riceve la richiesta (request)
# 2) prende i dati dal database
# 3) restituisce una pagina HTML (template) al browser
def product_list(request):
    # Query al database tramite ORM:
    # - filter(available=True) mostra solo prodotti "attivi"
    # - order_by("name") li ordina alfabeticamente
    products = Product.objects.filter(available=True).order_by("name")

    # render() prende:
    # - request
    # - nome del template HTML
    # - dizionario "context" con i dati da usare nel template
    return render(request, "catalog/product_list.html", {"products": products})


# Questa view mostra il dettaglio di un singolo prodotto.
# pk = primary key, cioè l'ID del prodotto nel database (es. /products/3/)
def product_detail(request, pk: int):
    # get_object_or_404 fa due cose:
    # - prova a prendere il prodotto richiesto
    # - se non esiste (o non è available), risponde automaticamente con una pagina 404
    product = get_object_or_404(Product, pk=pk, available=True)

    # Passiamo al template un singolo oggetto "product"
    return render(request, "catalog/product_detail.html", {"product": product})
