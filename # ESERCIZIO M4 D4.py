# ESERCIZIO M4_D4


# ESERCIZIO 1 PAG.2
""" Abbiamo la stringa: nome_scuola = "Epicode" Stampare ogni carattere della stringa, uno su ogni riga, 
utilizzando un costrutto for.
"""
nome_scuola = "esempio"
for carattere in nome_scuola:
    print(carattere)

#ESERCIZIO 2 PAG.3
""" Abbiamo una serie di simboli di elementi chimici (tutti da una sola lettera)
all'interno della variabile elementi:
elementi = "NPKOHC"
Stampare ogni elemento su una riga diversa.
"""
elementi = "NPKOHC"
for elemento in elementi:
    print(elemento)

#ESERCIZIO 3 PAG.4
""" Abbiamo una serie di simboli di elementi chimici (tutti da una sola lettera)
all'interno della variabile elementi:
elementi = "NPKOHC"
Stampare ogni elemento su una riga diversa, preceduto dalla scritta "elemento
–".
"""

elementi = "NPKOHC"
for elemento in elementi:
    print("ELEMENTO-" + elemento)

#ESERCIZIO 4 PAG.5
""" Abbiamo una serie di simboli di elementi chimici (tutti da una sola lettera)
all'interno della variabile elementi:
elementi = "NPKOHC"
Stampare ogni elemento su una riga diversa, preceduto dalla scritta "elemento
– numero n" dove al posto di n scriveremo un numero progressivo che parte
da 1.
"""

elementi = "NPKOHC"
for i, elemento in enumerate(elementi, start=1):
    print(f"ELEMENTO - NUMERO {i} {elemento}")

#ESERIZIO 5 PAG.6
""" Modificare la parola "marmalade" in modo sostituire le "e" con le "a" e
viceversa.
Salvare il risultato in una variabile e stamparla a video.
Fare diverse versioni:
• una con un ciclo for,
• una con un ciclo while,
• una con il metodo delle stringhe .replace().
"""

# una col il ciclo for
parola_originale = "marmalade"
parola_modificata = ""

for lettera in parola_originale:
    if lettera == "e":
        parola_modificata += "a"
    elif lettera == "a":
        parola_modificata += "e"
    else:
        parola_modificata += lettera

print(parola_modificata)


# una con un ciclo while
parola_originale = "marmalade"
parola_modificata = ""
indice = 0

while indice < len(parola_originale):
    lettera = parola_originale[indice]
    if lettera == "e":
        parola_modificata += "a"
    elif lettera == "a":
        parola_modificata += "e"
    else:
        parola_modificata += lettera
    indice += 1

print(parola_modificata)


# una con con il metodo delle stringhe .replace()
parola_originale = "marmalade"
parola_modificata = parola_originale.replace("e", "1").replace("a", "e").replace("1", "a")

print(parola_modificata)

# METODO ABBREVIATO
old_string = "Marmalade"
new_string = 'Mermelede'
stringa_risultante = old_string.replace(old_string,new_string)
print(stringa_risultante)

# ESERCIZIO 6 PAG.7
""" Calcolare e stampare tutte le prime 10 potenze di 2 utilizzando un ciclo for.
Utilizzeremo:
• la funzione range(), e.g.:
for contatore in range(10):
pass # modificare qui
"""

for contatore in range(10):
    potenza_di_due = 2 ** contatore
    print(f"2^{contatore} = {potenza_di_due}")

# ESERCIZIO 7 PAG.8
"""Calcolare (ma non stampare) le prime N potenze di 2; ognuna di esse andrà
memorizzata in coda a una lista.
Alla fine, stampare la lista risultante.
Realizzare due versioni:
• con un ciclo while,
• con un ciclo for.
"""

# VERSIONE WHILE 

N= int(input("Scrivi un numero intero N."))
x = 2
i = 0
lista_risultante = list ()

while i <= N:
    lista_risultante.append(x**i)
    i += 1

print(lista_risultante)


#VERSIONE FOR

N= int(input("Scrivi un numero intero N."))
x = 2
lista_risultante = list ()

for y in range(0,N+1):
    lista_risultante.append(x**y)

print(lista_risultante)


#ESERCZIO 8 PAG.9
"""Calcolare (ma non stampare) le prime N potenze di 3; ognuna di esse andrà
memorizzata in coda a una lista.
Alla fine, stampare la lista risultante.
Realizzare due versioni:
• con un ciclo while,
• con un ciclo for.
"""

#VERSIONE WHILE

N= int(input("Scrivi un numero intero N."))
x = 3
i = 0
lista_risultante = list ()

while i <= N:
    lista_risultante.append(x**i)
    i += 1

print(lista_risultante)


#VERSIONE FOR

N= int(input("Scrivi un numero intero N."))
x = 3
lista_risultante = list ()

for y in range(0,N+1):
    lista_risultante.append(x**y)

print(lista_risultante)

#ESERCIZIO 9 PAG.10
"""Calcolare (ma non stampare) le prime N potenze di K; ognuna di esse andrà
memorizzata in coda a una lista.
Alla fine, stampare la lista risultante.
Proviamo con diversi valori di K, oppure facciamola inserire all'utente.
Realizzare due versioni:
• con un ciclo while,
• con un ciclo for.
"""

#VERSIONE CON WHILE


N = int(input("Inserisci il numero di potenze da calcolare: "))  # Chiediamo all'utente il numero di potenze
K = int(input("Inserisci il valore di K: "))  # Chiediamo all'utente il valore di K
x = K
i = 0

lista_risultante = list ()

while i <= N:
    lista_risultante.append(x**i)
    i += 1

print(lista_risultante)


#VESRIONE CON FOR
N = int(input("Inserisci il numero di potenze da calcolare: "))  # Chiediamo all'utente il numero di potenze
K = int(input("Inserisci il valore di K: "))  # Chiediamo all'utente il valore di K
x = K

lista_risultante = list ()

for y in range(0,N+1):
    lista_risultante.append(x**y)

print(lista_risultante)

# ESERCIZIO 10 PAG.11
"""Calcolare e stampare tutte le potenze di 2 minori di 25000."""

x = 2
i = 0
while x**i <= 2500:
    print(x**i, " ", end="")
    i +=  1

#ESERCIZIO 11 PAG. 12
"""Calcolare e stampare tutte le potenze di 2 minori di un certo numero N."""

N= int(input("Scrivi un numero intero N."))
x =2
i = 0
while x**i <= N:
    print(x**i, " ", end="")
    i +=  1

#ESERCIZIO 12 PAG. 13
"""Calcolare e stampare tutte le prime 100 potenze di 2, ogni 3 (e.g. 2⁰, 2³, 2⁶, 2⁹,
…).
Oltre a stamparle, memorizzarle in coda a una lista e stamparla alla fine.
Usate due metodi diversi:
1. usare un costrutto for e range(100), e poi un costrutto if per visualizzare
e memorizzare solo ogni 3
2. usare un costrutto for e range(0, 100, 3)
"""

# Metodo 1
potenze_metodo1 = []

for i in range(100):
    potenza_di_2 = 2**i
    if i % 3 == 0:
        print(f"2^{i} = {potenza_di_2}")
        potenze_metodo1.append(potenza_di_2)

print("\nLista di potenze (Metodo 1):")
print(potenze_metodo1)

# Metodo 2
potenze_metodo2 = []

for i in range(0, 100, 3):
    potenza_di_2 = 2**i
    print(f"2^{i} = {potenza_di_2}")
    potenze_metodo2.append(potenza_di_2)

print("\nLista di potenze (Metodo 2):")
print(potenze_metodo2)

# ESERCIZIO 13 PAG.14
""" Abbiamo una lista con dei numeri:
numeri = [4, 9, 5, 1, 7, 10, 2, 3]
utilizzando un costrutto for, trovare il massimo di questa lista e stamparlo a 
video """

numeri = [4, 9, 5, 1, 7, 10, 2, 3]
massimo = numeri[0]

for numero in numeri:
    if numero > massimo:
        massimo = numero

print("Il massimo è:", massimo)

# ESERCIZIO 14 PAG.15
""" Abbiamo raccolto tutte le età degli studenti in una lista:
eta_studenti = [20, 30, 40, 50, 60]
utilizzando un ciclo for, calcolare la media delle età. Alla fine, stampa (a video) 
il risultato """

eta_studenti = [20, 30, 40, 50, 60]
somma_eta = 0

for eta in eta_studenti:
    somma_eta += eta

media_eta = somma_eta / len(eta_studenti)

print(media_eta)

# ESERCIZIO 15 PAG.16
""" Abbiamo una lista con i guadagni degli ultimi 12 mesi:
guadagni = [100, 90, 70, 40, 50, 80, 90, 120, 80, 20, 50, 
50]
usando un costrutto for, calcolare la media dei guadagni e stamparla a video.
"""
guadagni_mesi = [100, 90, 70, 40, 50, 80, 90, 120, 80, 20, 50, 50]
somma_guadagni = 0

for guadagni in guadagni_mesi:
    somma_guadagni += guadagni
    
media_guadagni = somma_guadagni / len(guadagni_mesi)

print(media_guadagni)

# ESERCIZIO 16 PAG. 17
""" Abbiamo una lista con i guadagni degli ultimi N mesi:
guadagni = [100, 90, 70, 40, 50, 80, 90, 120]
usando un costrutto for, calcolare la media dei guadagni e stamparla a video; 
stampare anche il numero di mesi considerati """

guadagni = [100, 90, 70, 40, 50, 80, 90, 120]
numero_mesi = len(guadagni)

somma_guadagni = 0

for guadagno in guadagni:
    somma_guadagni += guadagno

media_guadagni = somma_guadagni / numero_mesi

print(f"La media dei guadagni degli ultimi {numero_mesi} mesi è: {media_guadagni}")

# ESERCIZIO 17 PAG. 18
""" Abbiamo una lista di studenti:
studenti = ["Alex", "Bob", "Cindy", "Dan", "Emma", "Faith", "Grace", 
"Henry"]
utilizzare un ciclo for per stampare i nomi di tutti gli studenti con questa formattazione:
Studenti:
- Alex
- Bob
- Cindy """

lista_studenti = ["Alex", "Bob", "Cindy", "Dan", "Emma", "Faith", "Grace", "Henry"]

print("lista_studenti:")

for nome in lista_studenti:
    print(f"- {nome}")

# ESERCIZIO 18 PAG. 19
""" Abbiamo tre liste (sono tutte della stessa lunghezza):
studenti = ["Alex", "Bob", "Cindy", "Dan", "Emma", "Faith", "Grace", 
"Henry"]
corsi = ["Cybersecurity", "Data Analyst", "Backend", "Frontend", 
"Data Analyst", "Backend", "Frontend", "Cybersecurity"]
edizioni = [1, 2, 3, 2, 2, 1, 3, 3]
stampare a video, usando print(), ogni studente che corso segue e di che edizione, 
e.g.:
Alex segue Cybersecurity, edizione 1
Bob segue Data Analyst, edizione 2
...
facendo in modo che non ci sia uno spazio tra il corso e la virgola subito dopo """

studenti = ["Alex", "Bob", "Cindy", "Dan", "Emma", "Faith", "Grace", "Henry"]

corsi = ["Cybersecurity", "Data Analyst", "Backend", "Frontend", "Data Analyst", "Backend", 
         "Frontend", "Cybersecurity"]

edizioni = [1, 2, 3, 2, 2, 1, 3, 3]

for i in range(len(studenti)):
    print(f"{studenti[i]} segue {corsi[i]}, edizione {edizioni[i]}")

# ESERCIZIO 19 PAG. 20
""" Abbiamo una lista di parole:
parole = ["Albergo", "Sedia", "Borgo", "Petalo", 
"Belvedere", "Semestre", "Sosta", "Orpello", "Abete"]
stampiamo, per ogni parola, quante volte appare la lettera "e" """

parole = ["Albergo", "Sedia", "Borgo", "Petalo", "Belvedere", "Semestre", 
          "Sosta", "Orpello", "Abete"]

for parola in parole:
    conteggio_e = parola.lower().count('e')
    print(f"Nella parola '{parola}' appare la lettera 'e' {conteggio_e} volte.")

#ESERCIZIO 20 PAG. 21
""" Abbiamo una lista di parole:
parole = ["Albergo", "Sedia", "Borgo", "Petalo", "Eremo", 
"Belvedere", "Semestre", "Esteta", "Sosta", "Orpello", 
"Abete", "Orologio", "Cesta", "Ermellino"]
stampiamo, per ogni parola, quante volte appare la lettera "e"; facciamo 
attenzione al fatto che appare sia maiuscola che minuscola """

parole = ["Albergo", "Sedia", "Borgo", "Petalo", "Eremo", "Belvedere", "Semestre", 
          "Esteta", "Sosta", "Orpello", "Abete", "Orologio", "Cesta", "Ermellino"]

for parola in parole:
    conteggio_e = parola.lower().count('e')
    print(f"Nella parola '{parola}' appare la lettera 'e' {conteggio_e} volte.")

# ESERCIZIO 21 PAG. 22
""" Abbiamo una lista di codici fiscali:
lista_cf = ["ABCDEF95G01A123B", "GHIJKL91M02A321C", 
"MNOPQR89S03A456D", "STUVWX95Z04A654E", "XYZABC01D05A789F", 
"DEFGHI95J06A987G"]
trovare i codici fiscali che contengono "95", metterli in una lista, e alla fine 
stamparla """

lista_cf = ["ABCDEF95G01A123B", "GHIJKL91M02A321C", "MNOPQR89S03A456D", 
            "STUVWX95Z04A654E", "XYZABC01D05A789F", "DEFGHI95J06A987G"]
cf_contenenti_95 = []

for cf in lista_cf:
    if "95" in cf:
        cf_contenenti_95.append(cf)

print(cf_contenenti_95)

# ESERCIZIO 22 PAG. 23
""" Abbiamo una lista di codici fiscali:
lista_cf = ["ABCDEF95G01A123B", "GHIJKL91M02A321C", 
"MNOPQR89S03A456D", "STUVWX95Z04A654E", "XYZABC01D05A789F", 
"DEFGHI95J06A987G"]
Per ognuno di essi, stampare a video i caratteri relativi al nome e quelli relativi al 
cognome """

lista_cf = ["ABCDEF95G01A123B", "GHIJKL91M02A321C", 
"MNOPQR89S03A456D", "STUVWX95Z04A654E", "XYZABC01D05A789F", 
"DEFGHI95J06A987G"]

for cf in lista_cf:
    nome = cf[0:6]
    cognome = cf[6:15]
    print(f"Nome: {nome}, Cognome: {cognome}")

# ESERCIZIO 23 PAG. 24
""" Abbiamo tre liste della stessa lunghezza:
studenti = ["Alex", "Bob", "Cindy", "Dan", "Emma", "Faith", "Grace", 
"Henry"]
corsi = ["Cybersecurity", "Data Analyst", "Backend", "Frontend", 
"Data Analyst", "Backend", "Frontend", "Cybersecurity"]
edizioni = [1, 2, 3, 2, 2, 1, 3, 3]
dove ogni elemento nella medesima posizione si riferisce ai dati dello stesso studente. 
Stampare a video tutti e soli gli studenti che frequentano una prima edizione; utilizzare 
solo i dati necessari """

studenti = ["Alex", "Bob", "Cindy", "Dan", "Emma", "Faith", "Grace", "Henry"]
corsi = ["Cybersecurity", "Data Analyst", "Backend", "Frontend", 
         "Data Analyst", "Backend", "Frontend", "Cybersecurity"]
edizioni = [1, 2, 3, 2, 2, 1, 3, 3]

for i in range(len(studenti)):
    if edizioni[i] == 1:
        print(f"Lo studente {studenti[i]} frequenta la prima edizione del corso {corsi[i]}.")

# ESERCIIO 24 PAG. 25
""" Abbiamo tre liste della stessa lunghezza:
studenti = ["Alex", "Bob", "Cindy", "Dan", "Emma", "Faith", "Grace", 
"Henry"]
corsi = ["Cybersecurity", "Data Analyst", "Backend", "Frontend", 
"Data Analyst", "Backend", "Frontend", "Cybersecurity"]
edizioni = [1, 2, 3, 2, 2, 1, 3, 3]
Dove ogni elemento nella medesima posizione si riferisce ai dati dello stesso studente. 
Riuscite a vedere una similarità di qualche tipo con la logica che si usa in SQL e le tabelle 
relazionali? """

# Si effettivamente c'è una similarità con la logica che si usa in SQL.
# Se vogliamo possiamo paragonare le tre liste alle creazioni delle tabelle come in MYSQL 
# con i vari attributi all'interno di essa.

# ESERCIZIO 25 PAG. 26
""" Creiamo un dizionario che assegni ad ogni proprietario la sua auto, sapendo 
che:
• Ada guida una Punto
• Ben guida una Multipla
• Charlie guida una Golf
• Debbie guida una 107 Poi stampiamo il dizionario per intero, e poi l'auto 
associata a Debbie """

proprietari_auto = {
    'Ada': 'Punto',
    'Ben': 'Multipla',
    'Charlie': 'Golf',
    'Debbie': '107'
}
print(proprietari_auto)

auto_debbie = proprietari_auto['Debbie']
print(f"Debbie possiede una {auto_debbie}")

# ESERCIZIO 26 PAG. 27
""" Abbiamo un dizionario che assegni ad ogni proprietario la sua auto:
dizionario_auto = {"Ada": "Punto", "Ben": "Multipla", 
"Charlie": "Golf", "Debbie": "107"}
Aggiungere i proprietari Emily e Fred che posseggono rispettivamente una A1 e 
una Octavia; eliminare i dati relativi a Ben.
Stampare il dizionario per controllare che sia tutto corretto """

dizionario_auto = {"Ada": "Punto", 
                   "Ben": "Multipla", 
                   "Charlie": "Golf", 
                   "Debbie": "107",
                   "Emyly" : "A1" "Octavia",
                   "Fred"  : "A1" "Octavia"
}

del dizionario_auto ["Ben"]
print(dizionario_auto)

# ESERCIZIO 27 PAG. 28
""" Abbiamo due dizionari che assegnano ad ogni proprietario la propria auto:
dizionario_auto = {"Ada": "Punto", "Ben": "Multipla", 
"Charlie": "Golf", "Debbie": "107", "Emily": "A1"}
nuovi_proprietari = {"Ben": "Polo", "Fred": "Octavia", 
"Grace": "Yaris", "Hugh": "Clio"}
Aggiornare il dizionario dizionario_auto con i dati contenuti in 
nuovi_proprietari e stamparlo. Cosa è successo a Ben?
"""

dizionario_auto = {"Ada": "Punto", 
                   "Ben": "Multipla", 
                   "Charlie": "Golf", 
                   "Debbie": "107", 
                   "Emily": "A1"
}

nuovi_proprietari = {"Ben": "Polo", 
                     "Fred": "Octavia", 
                     "Grace": "Yaris",
                     "Hugh": "Clio"
}

dizionario_auto.update({"Ben": "Multipla","Ben": "Polo"})
 
print(dizionario_auto)

# ESERCIZIO 28 PAG.29
""" Abbiamo un dataset che assegna ad ogni proprietario la propria auto, in forma 
di dizionario:
dizionario_auto = {"Ada": "Punto", "Ben": "Multipla", 
"Charlie": "Golf", "Debbie": "107", "Emily": "A1", "Fred": 
"Octavia", "Grace": "Yaris", "Hugh": "Clio"}
Viene richiesto di ricercare in questo dataset i dati di Hugh, Ada, Emily e 
Debbie, e visualizzare le auto relativi """


dizionario_auto = {
    "Ada": "Punto",
    "Ben": "Multipla",
    "Charlie": "Golf",
    "Debbie": "107",
    "Emily": "A1",
    "Fred": "Octavia",
    "Grace": "Yaris",
    "Hugh": "Clio"
}

proprietari_da_cercare = ["Hugh", "Ada", "Emily", "Debbie"]


for proprietario in proprietari_da_cercare:
    if proprietario in dizionario_auto:
        auto = dizionario_auto[proprietario]
        print(f"{proprietario} guida una {auto}")
    else:
        print(f"{proprietario} non è presente nel dataset.")

# ESERCIZIO 29 PAG. 30
""" Abbiamo un dataset che assegna ad ogni proprietario la propria auto, in forma di 
dizionario:
dizionario_auto = {"Ada": "Punto", "Ben": "Multipla", "Charlie": 
"Golf", "Debbie": "107", "Emily": "A1", "Fred": "Octavia", "Grace": 
"Yaris", "Hugh": "Clio"}
Viene richiesto di ricercare in questo dataset i dati di Ada, Emily, Jade, Ben, Hugh, Kelly e 
Charlie, e visualizzare le auto relative.
Non tutti i dati potrebbero essere presenti nel dataset, quindi quando un nome non è 
presente visualizzeremo un messaggio adeguato """

dizionario_auto = {"Ada": "Punto", 
                   "Ben": "Multipla", 
                   "Charlie": "Golf", 
                   "Debbie": "107", 
                   "Emily": "A1", 
                   "Fred": "Octavia", 
                   "Grace": "Yaris", 
                   "Hugh": "Clio"
}

proprietari_da_cercare = ["Ada", "Emily", "Jade", "Ben", "Hugh", "Kelly", "Chary"]

for proprietario in proprietari_da_cercare:
    if proprietario in dizionario_auto:
        auto = dizionario_auto[proprietario]
        print(f"{proprietario} guida una {auto}")
    else:
        print(f"{proprietario} non è presente nel dataset.")

# ESERCIZIO 30 PAG. 31
""" Abbiamo un dizionario:
diz = {"a": 121, "zy": 3774, "qop": 147726, "ab": 328, "k": 
12, "clap": 9}
utilizzando il metodo .keys(), stampiamone tutte le chiavi """

diz = {"a": 121, 
       "zy": 3774,  
       "qop": 147726, 
       "ab": 328, 
       "k": 12, 
       "clap": 9
}

print(diz.keys())

# ESERCIZIO 31 PAG. 32
""" Abbiamo un dizionario:
diz = {"a": 121, "zy": 3774, "qop": 147726, "ab": 328, "k": 
12, "clap": 9}
utilizzando il metodo .values(), stampiamone tutte i valori """

diz = {"a": 121, 
       "zy": 3774,  
       "qop": 147726, 
       "ab": 328, 
       "k": 12, 
       "clap": 9
}

print(diz.values())

# ESERCIZIO 32 PAG. 33
""" Abbiamo un dizionario:
diz = {"a": 121, "zy": 3774, "qop": 147726, "ab": 328, "k": 
12, "clap": 9}
utilizzando il metodo dei dizionari .items() stampate le coppie chiave-valore 
presenti nel dizionario su righe diverse """

diz = {"a": 121, 
       "zy": 3774,  
       "qop": 147726, 
       "ab": 328, 
       "k": 12, 
       "clap": 9
}

for chiave, valore in diz.items():
    print(f"{chiave}: {valore}")

# ESERCIZIO 33 PAG. 34
""" Abbiamo un dizionario:
diz = {"a": 121, "zy": 3774, "qop": 147726, "ab": 328, "k": 
12, "clap": 9}
utilizzando il metodo dei dizionari .values(), calcolare il valore massimo, il 
valore minimo, la somma, e stampiamo i risultati """

diz = {"a": 121, 
       "zy": 3774,  
       "qop": 147726, 
       "ab": 328, 
       "k": 12, 
       "clap": 9
}

valori = list(diz.values())
valore_massimo = max(valori)
valore_minimo = min(valori)
somma = sum(valori)

print(f"Valore massimo: {valore_massimo}")
print(f"Valore minimo: {valore_minimo}")
print(f"Somma: {somma}")


# ESERCIZIO 34 PAG. 35
""" Abbiamo un dizionario che assegna ad ogni proprietario la sua auto:
dizionario_auto = {"Ada": "Punto", "Ben": "Multipla", 
"Charlie": "Golf", "Debbie": "107"}
Con un ciclo for, e usando il metodo .items(), stampiamo ogni proprietario 
e la sua auto, formattandolo come:
Ada guida una Punto
Ben guida una Multipla """

dizionario_auto = {"Ada": "Punto", 
                   "Ben": "Multipla", 
                   "Charlie": "Golf", 
                   "Debbie": "107"
}
proprietari = ["Ada","Ben","Charlie", "Debbie"]
auto = ["Punto","Multipla","Golf", "107"]

for proprietari, auto in dizionario_auto.items():
    print(f"{proprietari} guida una {auto}")

# ESERCIZIO 35 PAG. 36
""" Abbiamo un dizionario che assegna ad ogni proprietario la sua auto:
dizionario_auto = {"Ada": "Punto", "Ben": "Multipla", 
"Charlie": "Golf", "Debbie": "107"}
Con un ciclo, e usando il metodo .values(), stampiamo a video tutte le auto 
che non sono una Multipla """

dizionario_auto = {"Ada": "Punto", 
                   "Ben": "Multipla", 
                   "Charlie": "Golf", 
                   "Debbie": "107"
}

for auto in dizionario_auto.values():
    if auto != "Multipla":
        print(auto)

# ESERCIZIO 36 PAG. 37
""" Abbiamo i seguenti dati riguardo dei collezionisti e le loro collezioni:
• Ada ha 10 Funko Pop, 5 action figures e 35 manga
• Ben ha 2 Funko Pop, 6 action figures, 40 manga e 2 graphic novels
• Charlie ha 31 action figures e 18 graphic novels
• Debbie ha 1 Funko Pop, 9 graphic novels, 25 manga e 2 action figures
Creare dei dizionari innestati che contengano questi dati, e quindi visualizzarli """

collezioni = {
    "Ada": {
        "Funko Pop": 10,
        "Action Figures": 5,
        "Manga": 35
    },
    "Ben": {
        "Funko Pop": 2,
        "Action Figures": 6,
        "Manga": 40,
        "Graphic Novels": 2
    },
    "Charlie": {
        "Action Figures": 31,
        "Graphic Novels": 18
    },
    "Debbie": {
        "Funko Pop": 1,
        "Graphic Novels": 9,
        "Manga": 25,
        "Action Figures": 2
    }
}

# ESERCIZIO 37 PAG. 38
""" Abbiamo i seguenti dati riguardo dei collezionisti e le loro collezioni:
• Ada ha 10 Funko Pop, 5 action figures e 35 manga
• Ben ha 2 Funko Pop, 6 action figures, 40 manga e 2 graphic novels (entrambe 
della DC)
• Charlie ha 31 action figures e 18 graphic novels (di cui 10 della Marvel e 8 
della DC)
• Debbie ha 1 Funko Pop, 9 graphic novels (di cui 4 della DC e 5 della Marvel), 
25 manga e 2 action figures
Creare dei dizionari innestati che contengano questi dati, e quindi visualizzarli.
"""

collezioni = {
    "Ada": {
        "Funko Pop": 10,
        "Action Figures": 5,
        "Manga": 35
    },
    "Ben": {
        "Funko Pop": 2,
        "Action Figures": 6,
        "Manga": 40,
        "Graphic Novels": {
            "DC": 2
        }
    },
    "Charlie": {
        "Action Figures": 31,
        "Graphic Novels": {
            "Marvel": 10,
            "DC": 8
        }
    },
    "Debbie": {
        "Funko Pop": 1,
        "Graphic Novels": {
            "DC": 4,
            "Marvel": 5
        },
        "Manga": 25,
        "Action Figures": 2
    }
}

print(collezioni)

# ESERCIZIO 38 PAG. 39
""" Riguardo l'esercizio precedente, stampiamo le risposte a:
1. quanti Funko Pop ha Ada?
2. quanti manga ha Ben?
3. quante graphic novels della Marvel ha Debbie?
4. quanti Funko Pop hanno Ada e Ben in tutto?
5. quanti manga hanno in tutto i collezionisti?
6. quante graphic novel della DC hanno in tutto i collezionisti?
7. quante graphic novel hanno in tutto i collezionisti? """

collezioni = {
    "Ada": {
        "Funko Pop": 10,
        "Action Figures": 5,
        "Manga": 35
    },
    "Ben": {
        "Funko Pop": 2,
        "Action Figures": 6,
        "Manga": 40,
        "Graphic Novels": {
            "DC": 2
        }
    },
    "Charlie": {
        "Action Figures": 31,
        "Graphic Novels": {
            "Marvel": 10,
            "DC": 8
        }
    },
    "Debbie": {
        "Funko Pop": 1,
        "Graphic Novels": {
            "DC": 4,
            "Marvel": 5
        },
        "Manga": 25,
        "Action Figures": 2
    }
}

# DOMANDA NUM.1
funko_pop_ada = collezioni["Ada"]["Funko Pop"]
print(f"Ada ha {funko_pop_ada} Funko Pop.")

#DOMANDA NUM.2
manga_ben = collezioni["Ben"]["Manga"]
print(f"Ben ha {manga_ben} manga.")

#DOMANDA NUM.3
graphic_novels_marvel_debbie = collezioni["Debbie"]["Graphic Novels"]["Marvel"]
print(f"Debbie ha {graphic_novels_marvel_debbie} graphic novels della Marvel.")

#DOMANDA NUM.4
funko_pop_totale = collezioni["Ada"]["Funko Pop"] + collezioni["Ben"]["Funko Pop"]
print(f"Ada e Ben hanno in totale {funko_pop_totale} Funko Pop.")

#DOMANDA NUM.5
manga_totale = sum([collezioni[persona]["Manga"] for persona in collezioni])
print(f"I collezionisti hanno in totale {manga_totale} manga.")

#DOMANDAA NUM.6
dc_graphic_novels_totale = sum([collezioni[persona]["Graphic Novels"].get("DC", 0) for persona in collezioni])
print(f"I collezionisti hanno in totale {dc_graphic_novels_totale} graphic novels della DC.")

#DOMANDA NUM.7
graphic_novels_totale = sum([sum(collezioni[persona]["Graphic Novels"].values()) for persona in collezioni])
print(f"I collezionisti hanno in totale {graphic_novels_totale} graphic novels.")


























