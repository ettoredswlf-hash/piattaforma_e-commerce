# Piattaforma e-commerce con Python e Django

## Descrizione del progetto
Questo progetto è una piccola piattaforma e-commerce sviluppata con **Python** e **Django**, usando **SQLite** come database.  
L’applicazione permette di:

- visualizzare un **catalogo prodotti** (lista + dettaglio)
- gestire un **carrello** (basato su sessione)
- completare il **checkout** e creare un ordine (**Order** + **OrderItem**)
- **registrazione / login / logout**
- associare gli **ordini all’utente loggato** (“I miei ordini”)
- gestire prodotti e ordini tramite **Django Admin**

> Nota importante (traccia): **nomi di variabili/classi/file in inglese**, interfaccia utente in **italiano**.

---

## Struttura del progetto (apps Django)
- `catalog`: gestione prodotti e pagine pubbliche (lista/dettaglio)
- `shopping_cart`: carrello in sessione (add/remove/increase/decrease + totale)
- `orders`: checkout + creazione ordine + “I miei ordini”
- `accounts`: registrazione (signup) + integrazione auth di Django
- `templates/registration`: template login (Django auth)
- `static/css/styles.css`: stile grafico del sito

---

## Requisiti
- Python **3.10**
- Django **5.x**
- Pillow (per `ImageField`)
- Git

---

## Installazione e avvio (Windows / PowerShell)

### 1) Clona il repository
```bash
git clone https://github.com/ettoredswlf-hash/piattaforma_e-commerce.git
cd piattaforma_e-commerce
```

### 2) Crea e attiva un ambiente virtuale

**Opzione A — venv (consigliata)**
```bash
python -m venv .venv
.venv\Scripts\activate
```

**Opzione B — Conda (come nel mio caso)**
```bash
conda create -n ecommerce_env python=3.10 -y
conda activate ecommerce_env
```

### 3) Installa le dipendenze
Se è presente `requirements.txt`:
```bash
pip install -r requirements.txt
```

### 4) Migrazioni database
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5) Crea un superuser (Admin)
```bash
python manage.py createsuperuser
```

### 6) Avvia il server
```bash
python manage.py runserver
```

---

## URL utili
- Frontend: http://127.0.0.1:8000/
- Carrello: http://127.0.0.1:8000/cart/
- Admin: http://127.0.0.1:8000/admin/
- Login: http://127.0.0.1:8000/accounts/login/
- Signup: http://127.0.0.1:8000/accounts/signup/
- I miei ordini (solo loggato): http://127.0.0.1:8000/orders/my/

---

## Guida rapida (uso applicazione)

### A) Aggiungere prodotti (admin)
1. Vai su: http://127.0.0.1:8000/admin/
2. Accedi con il superuser
3. Inserisci prodotti (nome, prezzo, descrizione, immagini se previste, disponibilità)

### B) Flusso utente
- Home: visualizza prodotti  
- Dettaglio prodotto: aggiunge al carrello  
- Carrello: modifica quantità / rimuove  
- Checkout: inserisce dati cliente e conferma ordine  
- Se loggato: vede “I miei ordini” con storico e dettaglio  

---

## Screenshot (consegna)
Gli screenshot richiesti dalla consegna sono in: `docs/screenshots/`

- `01_home_product_list.png`
- `02_product_detail.png`
- `03_cart.png`
- `04_checkout.png`
- `05_order_created.png`
- `06_login.png`
- `07_admin_orders_1.png`
- `07_admin_orders_2.png`

---

## Note tecniche
- Carrello: salvato in **sessione** (non in DB)
- Ordini: salvati in DB (**Order** + **OrderItem**)
- Associazione ordine-utente: se l’utente è autenticato, l’ordine viene collegato al suo account
