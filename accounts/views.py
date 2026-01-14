from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect


# View di registrazione utente (signup).
# Usiamo UserCreationForm di Django perché:
# - valida username e password secondo le regole del progetto
# - salva l'utente in modo sicuro (password hashata, non in chiaro)
def signup(request):
    if request.method == "POST":
        # POST: l'utente ha inviato il form compilato
        form = UserCreationForm(request.POST)

        # is_valid() controlla: username, password, conferma password, regole password ecc.
        if form.is_valid():
            # Salva l'utente nel database (password salvata come hash)
            user = form.save()

            # login() crea la sessione di autenticazione: da questo momento request.user è autenticato
            login(request, user)

            # Dopo registrazione, rimandiamo alla lista prodotti
            return redirect("catalog:product_list")
    else:
        # GET: mostriamo un form vuoto
        form = UserCreationForm()

    # Se GET o POST con errori: renderizza la pagina con il form (e gli errori eventualmente)
    return render(request, "accounts/signup.html", {"form": form})
