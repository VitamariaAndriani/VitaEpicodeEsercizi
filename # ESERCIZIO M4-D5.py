# ESERCIZIO M4-D5

#ESERCIZIO 1 
""" Abbiamo una lista di numeri:
numeri = [4, 10, 50, 100, 128, 71, 46]
creare una nuova lista i cui elementi siano gli stessi di numeri incrementati di 10, 
mediante comprehension """

numeri = [4, 10, 50, 100, 128, 71, 46]
nuova_lista = [x + 10 for x in numeri]

# ESERCIZIO 2
""" Abbiamo una lista di numeri:
numeri = [4, 10, 50, 100, 128, 71, 46]
creare una nuova lista i cui elementi siano gli stessi di numeri ma raddoppiati, 
mediante comprehension """

numeri = [4, 10, 50, 100, 128, 71, 46]
nuova_lista = [x * 2 for x in numeri]
print(nuova_lista)

# ESERCIZIO 3
""" Abbiamo una lista di nomi:
nomi = ["Alex", "Bob", "Cindy", "Dan", "Emma", "Faith", 
"Grace", "Henry"]
creare una nuova lista i cui elementi siano le iniziali dei nomi, mediante 
comprehension """

nomi = ["Alex", "Bob", "Cindy", "Dan", "Emma", "Faith", "Grace", "Henry"]
iniziali = [nome[0] for nome in nomi]
print(iniziali)

# ESERCIZIO 4
""" Abbiamo una lista di nomi:
nomi = ["Alex", "Bob", "Cindy", "Dan", "Emma", "Faith", 
"Grace", "Henry"]
creare una nuova lista i cui elementi siano le iniziali dei nomi seguite da punto, 
mediante comprehension """

nomi = ["Alex", "Bob", "Cindy", "Dan", "Emma", "Faith", "Grace", "Henry"]
iniziali_con_punto = [nome[0] + '.' for nome in nomi]
print(iniziali_con_punto)

# ESERCIZIO 5
""" Abbiamo una lista di codici fiscali:
lista_cf = ["ABCDEF95G01A123B", "GHIJKL91M02A321C", 
"MNOPQR89S03A456D", "STUVWX95Z04A654E", "XYZABC01D05A789F", 
"DEFGHI95J06A987G"]
Creare una lista che contenga (per ogni CF) solo i caratteri relativi al nome, 
mediante comprehensio """

lista_cf = ["ABCDEF95G01A123B", "GHIJKL91M02A321C", "MNOPQR89S03A456D", 
            "STUVWX95Z04A654E", "XYZABC01D05A789F", "DEFGHI95J06A987G"]

nomi = [cf[0:6] for cf in lista_cf]
 
print(nomi)

# ESERCIZIO 6
""" Abbiamo una lista di codici fiscali:
lista_cf = ["ABCDEF95G01A123B", "GHIJKL91M02A321C", 
"MNOPQR89S03A456D", "STUVWX95Z04A654E", "XYZABC01D05A789F", 
"DEFGHI95J06A987G"]
Creare due liste, una che contenga (per ogni CF) solo i caratteri relativi al nome, 
e una che contenga (per ogni CF) solo i caratteri relativi al cognome; entrambe 
mediante comprehensio """

lista_cf = ["ABCDEF95G01A123B", "GHIJKL91M02A321C", 
"MNOPQR89S03A456D", "STUVWX95Z04A654E", "XYZABC01D05A789F", 
"DEFGHI95J06A987G"]
nomi = [cf[0:6]for cf in lista_cf]
cognomi = [cf[6:15] for cf in lista_cf]
print(nomi, cognomi)

# ESERCIZIO 7
""" Abbiamo una lista di codici fiscali:
lista_cf = ["ABCDEF95G01A123B", "GHIJKL91M02A321C", 
"MNOPQR89S03A456D", "STUVWX95Z04A654E", "XYZABC01D05A789F", 
"DEFGHI95J06A987G"]
Creare una lista che contenga solo i codici fiscali dei nati nel '95, tramite 
comprehension """

lista_cf = ["ABCDEF95G01A123B", "GHIJKL91M02A321C", "MNOPQR89S03A456D", 
            "STUVWX95Z04A654E", "XYZABC01D05A789F", "DEFGHI95J06A987G"]

cf_nati_95 = [cf for cf in lista_cf if cf[6:8] == '95']

print(cf_nati_95)

# ESERCIZIO 8
""" Abbiamo una lista di codici fiscali:
lista_cf = ["ABCDEF95G01A123B", "GHIJKL91M02A321C", 
"MNOPQR89S03A456D", "STUVWX95Z04A654E", "XYZABC01D05A789F", 
"DEFGHI95J06A987G"]
Creare una lista che contenga gli ultimi cinque caratteri dei soli codici fiscali di 
persone nate nel '95, tramite comprehension """

lista_cf = ["ABCDEF95G01A123B", "GHIJKL91M02A321C", "MNOPQR89S03A456D", 
            "STUVWX95Z04A654E", "XYZABC01D05A789F", "DEFGHI95J06A987G"]

ultimi_cinque_caratteri = [cf[-5:] for cf in lista_cf if cf[6:8] == '95']

print(ultimi_cinque_caratteri)

# ESERCIZIO 9
""" Abbiamo una lista di stringhe di prezzi in dollari, che erroneamente sono stati 
scritti con il simbolo dell'euro:
prezzi = ["100 €", "200 €", "500 €", "10 €", "50 €", "70 
€"]
cambiare il simbolo dell'euro (€) in quello del dollaro ($) per ogni stringa nella 
lista, usando la comprehension. """

prezzi = ["100 €", "200 €", "500 €", "10 €", "50 €", "70 €"]

prezzi_in_dollari = [prezzo.replace('€', '$') for prezzo in prezzi]

print(prezzi_in_dollari)

# ESERCIZIO 10
""" Abbiamo una lista di studenti:
studenti = ["Alex", "Bob", "Cindy", "Dan", "Emma", "Faith", 
"Grace", "Henry", "Isabelle", "John"]
vogliamo dividere gli studenti in due squadre per un campionato di Uno nel 
seguente modo: la prima metà per un squadra, e la seconda metà per l'altra.
Creiamo due liste per ogni squadra, e alla fine visualizziamole """

studenti = ["Alex", "Bob", "Cindy", "Dan", "Emma", "Faith", 
"Grace", "Henry", "Isabelle", "John"]

squadra_blu = ["Alex", "Bob", "Cindy", "Dan", "Emma"]
squadra_rossa = ["Faith", "Grace", "Henry", "Isabelle", "John"]

print(squadra_blu, squadra_rossa)

# ESRRCIZIO 11
""" Abbiamo una lista di studenti:
studenti = ["Alex", "Bob", "Cindy", "Dan", "Emma", "Faith", 
"Grace", "Henry", "Isabelle", "John"]
vogliamo dividere gli studenti in due squadre per un campionato di Uno nel 
seguente modo: selezioneremo i nomi in posizione pari per un squadra, e i nomi 
in posizione dispari per l'altra.
Creiamo due liste per ogni squadra, e alla fine visualizziamole """

studenti = ["Alex", "Bob", "Cindy", "Dan", "Emma", "Faith", "Grace", "Henry", "Isabelle", "John"]

squadra_pari = [studente for i, studente in enumerate(studenti) if i % 2 == 0]
squadra_dispari = [studente for i, studente in enumerate(studenti) if i % 2 != 0]

print("Squadra Pari:", squadra_pari)
print("Squadra Dispari:", squadra_dispari)

# ESERCIZIO 12
""" Abbiamo una lista con i guadagni degli ultimi 12 mesi (supponiamo da Gennaio a 
Dicembre):
guadagni = [100, 90, 70, 40, 50, 80, 90, 120, 80, 20, 50, 50]
dobbiamo confrontare, stampando tutto a video, il guadagno di ogni mese con la media 
dei guadagni precedenti
Esempio di un possibile output:
Mese 1: 100 €
Mese 2: 90 € (media prec: 100 €)
Mese 3: 70 € (media prec: 95 €) """

guadagni = [100, 90, 70, 40, 50, 80, 90, 120, 80, 20, 50, 50]

for i in range(len(guadagni)):
    mese = i + 1
    guadagno_mese = guadagni[i]
    media_precedenti = sum(guadagni[:i]) / i if i > 0 else 0
    
    print(f"Mese {mese}: {guadagno_mese} € (media prec: {media_precedenti:.2f} €)")

# ESERCIZIO 13
""" Abbiamo una lista con i guadagni degli ultimi 12 mesi (supponiamo da Gennaio 
a Dicembre):
guadagni = [100, 90, 70, 40, 50, 80, 90, 120, 80, 20, 50, 
50]
dobbiamo confrontare, stampando tutto a video, il guadagno di ogni mese con 
la media dei guadagni precedenti, e specificare nell'output se è maggiore o 
minore """

guadagni = [100, 90, 70, 40, 50, 80, 90, 120, 80, 20, 50, 50]

for i in range(len(guadagni)):
    mese = i + 1
    guadagno_mese = guadagni[i]
    media_precedenti = sum(guadagni[:i]) / i if i > 0 else 0
    
    if guadagno_mese > media_precedenti:
        confronto = "maggiore"
    elif guadagno_mese < media_precedenti:
        confronto = "minore"
    else:
        confronto = "uguale"
    
    print(f"Mese {mese}: {guadagno_mese} € (media prec: {media_precedenti:.2f} €) - Guadagno {confronto} della media precedente")

#ESERCIZIO 14
""" Scrivere una funzione che, data una lista di numeri, fornisca in output il 
maggiore di tutti, senza utilizzare la funzione max() """

lista_numeri = ["1010", "2025", "3003","4005","5045","6050","7050","8021","9023","10023"]


def trova_massimo(lista):
    massimo = float('-inf')  # Inizializziamo massimo con un valore molto basso
    for elemento in lista:
        numero = int(elemento)
        if numero > massimo:
            massimo = numero
    return massimo

massimo = trova_massimo(lista_numeri)
print(f"Il valore massimo è: {massimo}")

# ESERCIZIO 15
""" Scrivere una funzione che, data una lista di numeri, fornisca in output il minimo e 
il massimo (possiamo usare o meno le funzioni min() e max()) """

lista_numeri = [1010, 2025, 3003, 4005, 5045, 6050, 7050, 8021, 9023, 10023]

def trova_minimo_massimo(lista):
    minimo = lista[0]
    massimo = lista[0]

    for elemento in lista:
        if elemento < minimo:
            minimo = elemento
        if elemento > massimo:
            massimo = elemento

    return minimo, massimo


minimo, massimo = trova_minimo_massimo(lista_numeri)
print(f"Il valore minimo è: {minimo}")
print(f"Il valore massimo è: {massimo}")

# ESERCIZIO 16
""" Scrivere una funzione che, data una lista di numeri, fornisca in output i due 
numeri più grandi """

lista_numeri = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

def trova_due_numeri_piu_grandi(lista):
    if len(lista) < 2:
        return None  # Non ci sono abbastanza elementi nella lista

    primo_massimo = secondo_massimo = float('-inf')

    for numero in lista:
        if numero > primo_massimo:
            secondo_massimo = primo_massimo
            primo_massimo = numero
        elif primo_massimo > numero > secondo_massimo:
            secondo_massimo = numero

    return primo_massimo, secondo_massimo


due_numeri_piu_grandi = trova_due_numeri_piu_grandi(lista_numeri)
print(f"I due numeri più grandi sono: {due_numeri_piu_grandi}")

# ESERCIZIO 17
""" Scrivere una funzione che in input acquisisce una lista di numeri e un numero K; 
in output, dovrà restituire la media di tutti i numeri nella lista maggiori o uguali a 
K; se non ce ne dovesse essere nessuno, dovrà stampare a schermo un 
messaggio adeguato """

# Esempio di lista numeri
lista_numeri = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
K = 50

def media_maggiore_uguale_a_K(lista, K):
    somma = 0
    contatore = 0

    for numero in lista:
        if numero >= K:
            somma += numero
            contatore += 1

    if contatore == 0:
        print(f'Nessun numero maggiore o uguale a {K} trovato nella lista.')
        return None
    else:
        media = somma / contatore
        return media

risultato = media_maggiore_uguale_a_K(lista_numeri, K)

if risultato is not None:
    print(f'La media dei numeri maggiori o uguali a {K} è: {risultato}')

# ESERCIZIO 18
""" Scrivere una funzione che, data una lista di numeri, come output stamperà lo 
stesso numero di asterischi su righe diverse, ottenendo una semplice 
visualizzazione grafica
Esempio, supponendo di chiamare la funzione aster():
numeri = [5, 2, 3, 4]
aster(numeri)
Output:
*****
**
***
**** """

def aster(numeri):
    for numero in numeri:
        print('*' * numero)

# Esempio di utilizzo
numeri = [5, 2, 3, 4]
aster(numeri)

# ESERCIZIO 19
""" Abbiamo un testo, ad esempio:
- racconto = ""Lisetta va a passeggio in campagna; è felice di 
raccogliere i fiori che crescono sulle rive, ai bordi della strada. 
Ha già un bel mazzetto di ranuncoli e margherite.""
- Creiamo una funzione che prenda il testo in input, e in output ci dia un dizionario che 
contiene ogni tipo di carattere e quante volte appare. """

def conta_caratteri(testo):
    return {c: testo.lower().count(c) for c in set(testo.lower()) if c.isalnum()}

racconto = """Lisetta va a passeggio in campagna; è felice di 
raccogliere i fiori che crescono sulle rive, ai bordi della strada. 
Ha già un bel mazzetto di ranuncoli e margherite."""

risultato = conta_caratteri(racconto)
print(risultato)

# ESERCIZIO 20
""" Esercizio
Abbiamo un testo, ad esempio:
racconto = ""Lisetta va a passeggio in campagna; è felice di 
raccogliere i fiori che crescono sulle rive, ai bordi della strada. 
Ha già un bel mazzetto di ranuncoli e margherite.""
Creiamo una funzione che prenda il testo in input, e in output ci dia un dizionario che 
contiene ogni tipo di carattere e quante volte appare, esclusi punteggiatura e spazi. """

def conta_caratteri(testo):
    return {c: testo.count(c) for c in set(testo) if c.isalnum()}

testo = """Lisetta va a passeggio in campagna; è felice di 
raccogliere i fiori che crescono sulle rive, ai bordi della strada. 
Ha già un bel mazzetto di ranuncoli e margherite."""

risultato = conta_caratteri(testo)
print(risultato)


# ESERCIZIO 21
""" Abbiamo un testo, ad esempio:
racconto = ""Lisetta va a passeggio in campagna; è felice di 
raccogliere i fiori che crescono sulle rive, ai bordi della strada. 
Ha già un bel mazzetto di ranuncoli e margherite.""
Creiamo una funzione che prenda il testo in input, e in output ci dia un dizionario che 
contiene ogni tipo di carattere e quante volte appare, senza fare differenza tra maiuscole e 
minuscole """

def conta_caratteri(testo):
    return {c: testo.lower().count(c) for c in set(testo.lower()) if c.isalnum()}

racconto = """Lisetta va a passeggio in campagna; è felice di 
raccogliere i fiori che crescono sulle rive, ai bordi della strada. 
Ha già un bel mazzetto di ranuncoli e margherite."""

risultato = conta_caratteri(racconto)
print(risultato)


# ESERCIZIO 22
""" Andiamo su 
http://www.datiopen.it/it/opendata/Mappa_dei_pub_circoli_locali_in_Italia e 
scarichiamo la mappa dei pub, circoli e locali in Italia
Nota: per leggerlo nella funzione open() dovremo aggiungere il parametro 
encoding="latin1", ad esempio:
f = open(file_path, "r", encoding="latin1") """


import json

f = open("C:/Users/VITA MARIA/Downloads/Mappa-dei-pub-circoli-locali-in-Italia.json", "r", encoding="latin1")
mappe = json.load(f)

# 1: quanti dati ci sono in totale?
print(len(mappe)) 

# 2. Quali sono i metadati?
print(mappe[0].keys())

# 3. Stanpiano 11 primo elemento
print(mappe[0])

# 4. Stonpiano l’ultimo elemento
print(mappe[-1])

# 5. Riusciano a stampare un elemento a caso?
import random

pos = random. randint(0, len(mappe))
print(mappe[pos])

# 6. Quali sono gli anni di inserimento presenti?
set = set()
for x in mappe:
  set.add(x["canno_inserimento"])
print(set)

# 7. Quante attività ci sono nel quadrato di longitudine 9-10 e latitudine 45-46?
attivitapos = [dizionari["cnome"] 
               for dizionari in mappe 
               if 9 <= float(dizionari["clongitudine"]) <= 10 and 45 <= 
               float(dizionari["clatitudine"]) <= 46 ]

# 8. Quante attività ci sono nella provincia di Vicenza?
attivitaprov = [dizionari["cnome"] 
                for dizionari in mappe 
                if dizionari["cprovincia"].lower() == "vicenza"]

# 9. Quante enoteche ci sono, e come si chiamano?
enoteche = [dizionari["cnome"] 
            for dizionari in mappe 
            if dizionari["cnome"].lower().find("enoteca") != -1]

# 10. Quante attività ci sono in Lazio e Abruzzo assieme?
lazio_abruzzo = [dizionari["cnome"] 
                 for dizionari in mappe 
                 if dizionari["cregione"].lower() == "abruzzo" 
                 or dizionari["cregione"].lower() == "lazio"]





    


















