# Liste e dizionari

 ## Le liste in Python

Le **Liste** sono dei **contenitori** che raccolgono sequenze ordinate di informazioni. 

Possono contenere sequenze ordinate di numeri, di stringhe, di dizionari ecc.

Pensiamo alla **lista** dei partecipanti ad un *webinar*, composta, per semplicità, da 5 **stringhe** contenenti ciascuna nome e cognome.

Se dovessimo rappresentare la **lista** in un documento di testo, probabilmente scriveremmo:

- Mario Rossi
- Mario Verdi
- Luca Rossi
- Luca Bianchi
- Simone Verdi

In **Python** la lista viene rappresentata come una **sequenza** racchiusa da due parentesi quadre e dove ogni elemento della lista è separato dal successivo tramite una virgola.

```python
# questa è una lista in python
# trattandosi di stringhe, i caratteri sono racchiusi da due apostrofi o due virgolette.
lista = ['Mario Rossi', 'Mario Verdi', 'Luca Rossi', 'Luca Bianchi', 'Simone Verdi']
```

Dal punto di vista della rappresentazione delle informazioni, la **lista**, come abbiamo detto, è una **sequenza ordinata**, dove ad ogni elemento corrisponde un indice ben preciso, come da seguente tabella:

| Indice | Contenuto    |
| ------ | ------------ |
| 0      | Mario Rossi  |
| 1      | Mario Verdi  |
| 2      | Luca Rossi   |
| 3      | Luca Bianchi |
| 4      | Simone Verdi |

Notare, come abbiamo già visto per le stringhe, che l'indice parte dal numero 0.

A cosa ci serve l'indice? 

Ci serve per accedere all'elemento associato a un particolare indice.

Possiamo, semplicemente leggerne il contenuto, ma possiamo anche modificarlo.

```python
# con lista[i] accediamo all'elemento posto alla posizione i
print(lista[3])
# l'output sarà 'Luca Bianchi'

# con questa istruzione modifichiamo il contenuto dell'elemento da 'Luca Bianchi' a 'Roberto Alma'
lista[3] = 'Roberto Alma'
# ora l'output atteso sarà 'Roberto Alma'
print(lista[3])
```

Come facciamo a visualizzare tutti gli elementi di una **lista**? 

La risposta è semplice, utilizziamo un ciclo **for**, con la seguente sintassi:

```python
# ciclo for
# per ogni elemento che è presente nella lista
for element in lista:
  	# stampa l'elemento corrente
    print(element)
```

Logicamente, nel momento in cui abbiamo accesso alla **variabile** `element` possiamo eseguire qualsiasi istruzione che abbia ad oggetto `element`. Per assurdo, se si trattasse di una lista di indirizzi email, potremmo chiedere allo *script* di inviare una mail, con un determinato contenuto a ciascun indirizzo email.

E se volessimo verificare se un certo elemento è presente nella lista?

Potremmo utilizzare sempre un ciclo **for**:

```python
# ciclo for
# per ogni elemento che è presente nella lista
found = False
for element in lista:
  	if element == 'Massimiliano Nicotra':
      	print('L\'elemento è nella lista')
        found = True
        break
        
 # terminata la scansione della lista
if not found:
  	print('L\'elemento non è presente!')
```

Facciamo un test:

![](/Users/Roberto/Documents/progetti/corso-informatica-avvocati/static/python/check_list.png)

Ma avremmo potuto utilizzare una sintassi più coincisa ed elegante:

```python
lista = ['Mario Rossi', 'Mario Verdi', 'Luca Rossi', 'Luca Bianchi', 'Simone Verdi']

if 'Massimiliano Nicotra' in lista:
    print('trovato')
else:
    print('non trovato')
```

Ed, infatti:

![](/Users/Roberto/Documents/progetti/corso-informatica-avvocati/static/python/check_list2.png)

Per aggiungere elementi alla lista ci sono due possibilità:

- utilizzare il metodo `.append(element)` che aggiunge *element* alla fine della lista;
- utilizzare il metodo `.insert(position, element)` che inserisce *element* alla posizione indicata come primo parametro, spostando tutti gli elementi di una posizione.

```python
# aggiungo Massimiliano alla fine della lista
lista.append('Massimiliano Nicotra')
# ora Massimiliano sarà nella posizione 5 (ossia l'elemento n. 6)
```

| Indice | Contenuto                |
| ------ | ------------------------ |
| 0      | Mario Rossi              |
| 1      | Mario Verdi              |
| 2      | Luca Rossi               |
| 3      | Luca Bianchi             |
| 4      | Simone Verdi             |
| **5**  | **Massimiliano Nicotra** |

```python
# aggiungo Roberto Alma alla posizione 4
lista.insert(4, 'Roberto Alma')
# ora Massimiliano sarà nella posizione 4 (corrispondente all'elemento n. 5)
```

| Indice | Contenuto            |
| ------ | -------------------- |
| 0      | Mario Rossi          |
| 1      | Mario Verdi          |
| 2      | Luca Rossi           |
| 3      | Luca Bianchi         |
| **4**  | **Roberto Alma**     |
| 5      | Simone Verdi         |
| 6      | Massimiliano Nicotra |

Per eliminare un elemento, invece, si utilizza:

-  l'istruzione `pop(posizione)` che elimina l'elemento trovato alla posizione indicata, spostando di conseguenza gli altri.
- l'istruzione `remove(element)` che rimuove l'elemento che ha il valore indicato.

```python
# rimuove l'elemento alla posizione 4
lista.pop(4) # rimuove Roberto Alma

lista.remove('Massimiliano Nicotra') # rimuove Massimiliano Nicotra

# se però l'elemento indicato come parametro del metodo remove non è presente, il sistema restituisce una eccezione, per cui è bene utilizzare una istruzione condizionale
if 'Massimiliano Nicotra' in lista:
 		lista.remove('Massimiliano Nicotra')
```

Si può anche **copiare una lista** o **creare una lista che contenga gli stessi elementi**. Vediamo le differenze.

```python
# copia lista in nuova lista
nuova_lista = lista
# entrambe le variabili fanno riferimento agli stessi dati.
# se elimino un elemento da una, ciò avrà effetti anche sull'altra.
print(lista(0))
nuova_lista.pop(0)
print(lista(0))
```

Come vediamo, l'elemento in posizione 0 nella variabile `lista` prima era 'Mario Rossi', poi è divenuto 'Mario Verdi' (ossia quello che era in posizione 1).

Questo perché `lista` e `nuova_lista` si riferiscono allo stesso oggetto in memoria.

![](/Users/Roberto/Documents/progetti/corso-informatica-avvocati/static/python/change_lista1.png)

Utilizzando, invece, l'istruzione `list(elements)` verrà generata una nuova lista che non si riferisce più a quella precedente.

```python
# creo una nuova lista con gli stessi elementi
nuova_lista = list(lista)
# entrambe le liste però sono indipendenti
print(lista(0))
nuova_lista.pop(0)
print(lista(0))
```

Come vediamo, la variabile `lista` non è stata minimamente intaccata dalle operazioni su `nuova_lista`.

![](/Users/Roberto/Documents/progetti/corso-informatica-avvocati/static/python/change_lista2.png)

Infine, illustriamo la **concatenazione** della lista, molto utile per unire due liste.

```python
lista1 = ['Roberto', 'Massimiliano']
lista2 = ['Giovanni', 'Marco']
lista3 = lista1 + lista2
print(lista3)
```

Come vediamo ora abbiamo `list3` che è una nuova lista, contenente tutti gli elementi di `lista1` e di `lista2`.

![](/Users/Roberto/Documents/progetti/corso-informatica-avvocati/static/python/change_lista3.png)

