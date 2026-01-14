 ##piattaforma e-commerce utilizzando Python e Django


## Descrizione del progetto
Questo progetto è una piccola piattaforma e-commerce sviluppata con Python e Django utilizzando **SQLite** come database.
L’applicazione permette di:
- visualizzare un catalogo prodotti con pagina lista e pagina dettaglio
- gestire un carrello 
- creare un ordine a partire dal carrello (checkout)
- registrare/login/logout utenti e associare gli ordini agli utenti autenticati
- gestire prodotti e ordini dal pannello Django Admin

Struttura a app Django:
- `catalog`: gestione prodotti e pagine pubbliche
- `shopping_cart`: carrello session-based (add/remove/update/total)
- `orders`: creazione ordini e righe ordine (Order + OrderItem)
- `accounts`: registrazione utente (signup) e integrazione auth di Django

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
