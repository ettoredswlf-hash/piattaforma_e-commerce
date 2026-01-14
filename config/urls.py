"""
URL configuration for config project.

Questo file è il "centralino" delle URL:
decide quale app riceve le richieste in base al prefisso dell'URL.
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Pannello di amministrazione Django
    path("admin/", admin.site.urls),

    # Catalogo prodotti: homepage e pagine prodotto
    path("", include("catalog.urls")),

    # Carrello (session-based)
    path("cart/", include("shopping_cart.urls")),

    # Ordini (checkout + conferma)
    path("orders/", include("orders.urls")),

    # Registrazione (signup) gestita dalla nostra app accounts
    path("accounts/", include("accounts.urls")),

    # Login/Logout/Password reset di Django (URL già pronti)
    # Esempi:
    # /accounts/login/
    # /accounts/logout/
    path("accounts/", include("django.contrib.auth.urls")),
]

# In DEBUG Django può servire i file media (immagini caricate).
# In produzione i media vanno serviti da un web server (es. Nginx) o storage esterno.
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
