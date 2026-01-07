from django.shortcuts import get_object_or_404, render
from .models import Product


def product_list(request):
    products = Product.objects.filter(available=True).order_by("name")
    return render(request, "catalog/product_list.html", {"products": products})


def product_detail(request, pk: int):
    product = get_object_or_404(Product, pk=pk, available=True)
    return render(request, "catalog/product_detail.html", {"product": product})
