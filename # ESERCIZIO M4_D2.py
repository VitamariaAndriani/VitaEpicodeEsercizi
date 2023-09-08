# ESERCIZIO M4_D2

#TRACCIA 1. Creare una variabile che contiene la stringa "Epicode", quindi stamparla a video

stringa = "La scuola di Epicode"
print(stringa)

# TRACCIA 2. Abbiamo la stringa: nome_scuola = "Epicode". Stampare l'iniziale.

nome_scuola = "Epicode"
prima_lettera = nome_scuola[0]
print(prima_lettera)

# TRACCIA 3. Abbiamo la stringa: nome_scuola = "Epicode" Stampare le prime tre lettere.

nome_scuola = "Epicode"
prime_tre_lettere = nome_scuola[0:3]
print(prime_tre_lettere)

# TRACCIA 4. Abbiamo la stringa: nome_scuola = "Epicode" Stampare la stringa trasformando tutte le lettere in maiuscole.

nome_scuola = "Epicode"
stringa_maiuscole = nome_scuola.upper()
print(stringa_maiuscole)

# TRACCIA 5. Abbiamo la variabile: x = 10 Incrementarla di 2 e poi moltiplicarla per 3 Usare due metodi diversi!

x = 10
x += 2  # Incremento x di 2
x *= 3  # Moltiplico x per 3
print(x)

x = 10
x = (x + 2) * 3  # Incremento di 2 e poi moltiplicazione per 3
print(x)


# TRACCIA 6. Scriviamo un programma che chiede all'utente in input:
# • i litri di benzina nel serbatoio
# • l'efficienza espressa in km per litro
# • il prezzo della benzina per litrI
# quindi visualizza il costo per 100 km

litri_benzina = float(input("Litri di benzina nel serbatoio: "))
efficienza= float(input("Efficienza (km per litro): "))
prezzo = float(input("Prezzo della benzina al litro (in euro): "))
print("il costo per 100 km del tuo viaggio sarà:", (prezzo /efficienza * 10),"Euro")


# TRACCIA 7. Scriviamo un programma che chiede in input all'utente una stringa e visualizza i
 # primi 3 caratteri, seguiti da 3 punti di sospensione e quindi gli ultimi 3 caratteri.

def manipolazione_stringa():
    stringa = input("Inserisci la stringa che vuoi manipolare: \n")
    print(stringa[0:3] + "..." + stringa [-3:])

manipolazione_stringa()

# TRACCIA 8. Verificare, per ognuna delle seguenti stringhe, se il numero di caratteri è compreso tra 5 e 8:
# • Epicode
# • Windows
# • Excel
# • Powerpoint
# • Word
lista_stringhe = ['Epicode' ,'Windows', 'Excel', 'Powerpoint', 'Word' ]
for i in lista_stringhe:
    print("La lunghezza della parola ì'", i, "'è :",len(i))
    if 5 <=len(i) <=8:
        print("Compreso\n")
    else:
        print("Non Compreso\n")

# TRACCIA 9. Abbiamo la seguente lista di codici prodotto:
# codici = ["knt-S1", "cba-G9", "qtr-Z8"]
# Per ognuno dei codici, estrarre la parte finale (gli ultimi tre caratteri, quindi
# trattino incluso) e memorizzarlo in tre variabili

codici= ["knt-S1", "cba-G9","qtr-Z8"]
cod1=codici[0][-3:]
cod2= codici[1][-3:]
cod3= codici[2][-3:]
print(cod1, " ", cod2, " ", cod3, "\n")

# TRACCIA 10.Abbiamo un insieme (set) di titoli di azioni "growth" (cioè che hanno una crescita dei
# ricavi maggiore della media):

growth = {"Tesla", "Shopify", "Block", "Etsy", "MercadoLibre",
"Netflix", "Amazon", "Meta Platforms", "Salesforce", "Alphabet"}

# TRACCIA 11. Abbiamo un insieme di titoli "value" (cioè titoli che offrono agli investitori un elevato
# ritorno sull’investimento, garantendo al contempo stabilità e sicurezza):

value = {"Pfizer", "Johnson & Johnson", "JPMorgan Chase & Co.",
"Wells Fargo & Co.", "Verizon Communications", "BP PLC",
"LyondellBasell Industries", "MetLife", "Interactive Brokers Group",
"Intel"}

# TRACCIA 12. Abbiamo un insieme di titoli di aziende ad alta tecnologia:

tech = {"Apple", "Microsoft", "Alphabet", "Amazon", "NVIDIA", "Meta Platforms", 
        "Tesla", "Alibaba", "Salesforce", "Advanced Micro Devices",
          "Intel", "PayPal", "Activision Blizzard", "Electronic Arts",
            "The Trade Desk", "Zillow Group", "Match Group", "Yelp"}

# TRACCIA 13. Abbiamo un insieme di titoli di aziende nell'healthcare:

healthcare = {"UnitedHealth Group", "Johnson & Johnson", 
              "Eli Lilly & Co.", "Novo Nordisk", "Merck & Co.", "Roche Holding", 
              "Pfizer", "Thermo Fisher Scientific", "Abbott Laboratories"}

# TRACCIA 14. Un investitore vuole sapere:
# • se vuole diversificare l'investimento, investendo in aziende growth e value, quali sono le aziende?
# • quali sono le aziende tecnologiche growth?
# • se vuole investire sia in aziende tecnologiche che value, quali deve considerare?
# • quali sono i titoli healthcare che non sono value?
# • ci sono aziende sia tech che healthcare?
# • in quali deve investire se vuole azioni tech ma solo se siano growth o value?

print("Per diversificare l'investimento, investendo in azienda growth e value, investire nelle seguenti aziende:", growth | value)

print("Per diversificare l'investimento, investendo in azienda growth e value, investire nelle seguenti aziende: ", growth.union(value))

print("Le aziende tecnologiche growth sono le seguenti:", growth & tech)

print("Le aziende tecnologiche growth sono le seguenti:", growth.intersection(tech))

print("Le aziende tecnologiche growth sono le seguenti:", value & tech)

print("Le aziende tecnologiche growth sono le seguenti:", value.intersection(tech))

print("Le aziende tecnologiche growth sono le seguenti:", healthcare - value)

print("Le aziende tecnologiche growth sono le seguenti:", healthcare.difference(value))

print("Le aziende tecnologiche growth sono le seguenti:", tech & healthcare)

print("Le aziende tecnologiche growth sono le seguenti:"), tech.intersection((healthcare))























