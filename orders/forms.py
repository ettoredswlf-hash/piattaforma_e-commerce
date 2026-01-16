from django import forms
from .models import Order


# ModelForm = form costruito automaticamente partendo da un modello Django.
# Vantaggi:
# - genera in automatico i campi HTML
# - gestisce validazione base (email valida, max_length, campi obbligatori)
# - se form.is_valid() allora puoi salvare direttamente nel DB con form.save()
class OrderCreateForm(forms.ModelForm):
    class Meta:
        # Indichiamo quale modello usare come "base" del form
        model = Order

        # Selezioniamo SOLO i campi  che vogliamo far compilare al cliente).
        # NON includiamo campi tecnici come created_at/updated_at/paid/user perché li gestiamo noi nel backend.
        fields = ["name", "surname", "email", "address"]
        labels = {"name": "Nome",
                  "surname": "Cognome",
                  "email": "Email",
                  "address": "Indirizzo",

        }
