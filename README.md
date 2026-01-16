# Piattaforma e-commerce con Python e Django

## Descrizione del progetto
Questo progetto è una piccola piattaforma e-commerce sviluppata con Python e Django, utilizzando SQLite come database.
L’applicazione permette di:
- visualizzare un catalogo prodotti con pagina lista e pagina dettaglio
- gestire un carrello (session-based)
- creare un ordine a partire dal carrello (checkout)
- registrazione / login / logout utenti e associazione ordini agli utenti autenticati
- gestione prodotti e ordini dal pannello Django Admin

### Struttura app Django
- `catalog`: gestione prodotti e pagine pubbliche
- `shopping_cart`: carrello session-based (add/remove/increase/decrease/total)
- `orders`: creazione ordini e righe ordine (Order + OrderItem) + pagina "I miei ordini"
- `accounts`: registrazione utente (signup) + integrazione auth di Django

> Nota: nomi di classi, variabili e file sono in inglese , mentre l’interfaccia è in italiano.

---

## Requisiti
- Python **3.10**
- Django **5.x**
- Pillow (per ImageField)
- Git

---

## Installazione e avvio (Windows / PowerShell con Conda)

### 1) Clona la repository
```bash
git clone https://github.com/ettoredswlf-hash/piattaforma_e-commerce.git
cd piattaforma_e-commerce
