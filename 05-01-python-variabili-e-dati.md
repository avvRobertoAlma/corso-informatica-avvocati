# Python - Variabili e Tipi di Dati

## Le Variabili

In **Python**, come in qualsiasi altro linguaggio di programmazione, i dati vengono generalmente immagazzinati all'interno di **variabili**.

> Da un punto di vista meramente tecnico, una **variabile** è una *posizione, all'interno della memoria del computer, in cui è possibile archiviare informazioni durante l'esecuzione di un programma*.

Per illustrare il concetto in modo semplice a dei giuristi, si può immaginare la **variabile** come la **definizione** di un concetto all'interno di una disposizione normativa o di un contratto.

Se all'interno di un contratto, utilizzassi il seguente enunciato:

*Applicazione, si intende il programma informatico realizzato da Alfa S.r.l. e contraddistinto dal nome commerciale "YOULAWYER", disponibile per dispositivi smartphone (Android e iOS) comprensivo delle interfacce e di tutti gli elementi grafici;*

e poi in una clausola scrivessi:

*l'Utilizzatore riconosce la piena esclusiva titolarità dei diritti sull'**Applicazione** in capo al Fornitore*

è evidente che nella clausola il termine **Applicazione** deve intendersi riferito alla nozione di **Applicazione** come definito sopra.

In informatica, il concetto di **variabile** è lo stesso di quello delle definizioni di un contratto all'interno di un provvedimento normativo o di un contratto.

Ipotizziamo il seguente semplicissimo *script*:

```python
# definiamo il contenuto della variabile applicazione.
# la variabile applicazione contiene dati di tipo stringa
applicazione = "si intende il programma informatico realizzato da Alfa S.r.l. e contraddistinto dal nome commerciale \"YOULAWYER\", disponibile per dispositivi smartphone (Android e iOS) comprensivo delle interfacce e di tutti gli elementi grafici"

# la funzione print stampa i dati archiviati all'interno della variabile applicazione.
print(applicazione)
```

Il funzionamento è molto intuitivo. Abbiamo **dichiarato** una variabile `applicazione` che contiene del testo. Con l'invocazione della funzione `print()` (una funzione di Python), stiamo semplicemente chiedendo di stampare a video il contenuto della variabile `applicazione` ossia il testo ivi archiviato.

Ma come si crea una variabile ?

In **Python** la variabile deve essere **dichiarata** ed **inizializzata**, prima di poterla utilizzare.

```python
# enunciato di assegnazione
# la sintassi è nomevariabile = valore
# nomevariabile è il nome della variabile
# valore è il suo contenuto
# in questo caso il nome della variabile è 'nome' ed il contenuto è 'Roberto'
nome = 'Roberto'
```

> Per chi volesse approfondire, in altri linguaggi (es. javascript) è possibile dichiarare una variabile senza assegnare il valore. 
>
> Esempio, il seguente codice è un codice valido in *Javascript*
>
> ```javascript
> # dichiaro la variabile nome
> let nome;
> # assegno il valore
> nome = 'Roberto'
> ```

**Attenzione**, se provassimo ad utilizzare una **variabile**, senza averla prima dichiarata ed inizializzata, otterremmo con ogni probabilità un errore.

![](/Users/Roberto/Documents/progetti/corso-informatica-avvocati/static/python/variabile_non_dichiarata.png)

In questo caso nel file `errors.py` abbiamo semplicemente inserito:

```python
print(nome)
```

Ma il sistema, giustamente, non ha mai sentito parlare prima della **variabile** `nome` che è per lui fondamentalmente sconosciuta.

Un ragionamento identico si potrebbe porre, con le dovute distinzioni del caso, per il caso della definizione **Applicazione** di cui abbiamo parlato prima.

Se in una clausola contrattuale utilizzassi la parola **Applicazione** senza averla definita, la clausola potrebbe essere comunque valida, fermo restando che potrebbe ingenerare nell'interprete un fondato dubbio sull'applicazione cui ci si riferirebbe. Ma si 

La differenza fondamentale è che lo *script* non può funzionare correttamente in assenza della preventiva dichiarazione ed inizializzazione della **variabile**.

La **variabile** in Python può essere oggetto di assegnazione di un nuovo valore.

```python
# prima assegnazione
nome = 'Roberto'
# seconda assegnazione
nome = 'Massimiliano'
```

## Tipi di Dati

In informatica è fondamentale comprendere il concetto di **tipo di dato**.

Un dato afferente ad un certo **tipo** potrà essere oggetto di alcune operazioni piuttosto che altre.

Ad esempio, con le **stringhe** si potranno effettuare operazioni che non saranno, invece, possibili con i **numeri**.

### Numeri

In Python abbiamo sia **numeri interi** (*int*) sia **numeri in virgola mobile** (*float*), sui quali possiamo eseguire le operazioni aritmetiche classiche:

```python
# somma restituisce 2
print(1+1)
# sottrazione restituisce 0
print(2-2)
# moltiplicazione restituisce 4
print(2*2)
# divisione restituisce 4
print(8/2)
# divisione intera (ignora il resto), restituisce 1
print(7//5)
# resto della divisione, restituisce 2
print(7%5)
# elevamento a potenza, restituisce 8
print(2**3)
```

Possiamo poi utilizzare alcune **funzioni** specifiche per i **numeri**, come `round` che, sostanzialmente, effettua gli arrotondamenti.

```python
# restituisce il numero intero più vicino: 9
print(round(8.56))
# arrotonda a 2 cifre decimali: 8.57
print(round(8.567))
```

Oppure possiamo utilizzare `min` e `max` che, rispettivamente, restituiscono il minore e il maggiore tra i numeri utilizzati come argomenti della funzione.

```python
# minimo = 2
print(min(2, 5, 7))
# massimo = 7
print(max(2, 5, 7))
```

Altre funzioni possono essere utilizzate importando il **modulo** `math`.

### Stringhe

La **stringa** è fondamentalmente una sequenza di **caratteri**.

```python
# è una stringa
# possiamo utilizzare come delimitatori o una coppia di apostrofi o di virgolette
nome = 'Roberto'
```

Anche nel caso delle **stringhe** abbiamo la possibilità di avvalerci di **funzioni** specifiche.

```python
# la funzione len(string) restituisce il numero di caratteri (spazi compresi) di una stringa, in questo caso 7
print(len('Roberto'))
```

Importantissima è la **concatenazione**, ossia il modo di unire due differenti **stringhe**.

```python
# produce 'RobertoAlma'
print('Roberto'+'Alma')
# produce 'Roberto Alma'
print('Roberto' + ' ' +'Alma')
# sempre 'Roberto Alma'
nome = 'Roberto'
cognome = 'Alma'
print(nome + ' ' + cognome)
```

Attenzione: la **concatenazione** opera solo tra **stringhe**, non tra **stringhe** e dati di tipo diverso. Ad esempio, per concatenare **stringhe** e **numeri** è necessario convertire il numero in stringa, con la funzione `str(num)` che restituisce il numero convertito in stringa.

```python
# restituisce errore
print('Roberto ha ' + 35 + ' anni')

# non restituisce errore
print('Roberto ha ' + str(35)  + ' anni')
```

Possiamo accedere ai singoli caratteri di una **stringa** utilizzando gli indici.

> In generale, in informatica le sequenze di dati sono rappresentabili come delle sequenze ordinate di contenitori, ognuno dei quali ha un numero che parte da 0. 
> Utilizzando uno *pseudocodice* possiamo dire che:

*data una sequenza N di contenitori, 
possiamo accedere al primo elemento del contenitore, utilizzando l'espressione `N[0]`*

```python
# accede al primo carattere della stringa
nome = 'Roberto'

# restituisce 'R'
print(nome[0])

```

Le **stringhe** inoltre, oltre ad avere funzioni specifiche, consentono di utilizzare dei **metodi** sul singolo oggetto **stringa**.

La differenza tra **metodo** e **funzione** può essere definita nel seguente modo:

*la **funzione** è un'operazione a sé stante, il **metodo** è una sequenza di istruzioni che può essere applicata solo a quel determinato oggetto di tipo **stringa***

```python
nome = 'Roberto'
# questa è una funzione
# stampa la lunghezza di qualsiasi sequenza di informazioni
# in questo caso stampa il numero di caratteri della stringa nome ossia 7
print(len(nome))

# questo è un metodo
# può essere applicato solo ad un oggetto stringa come nome
# restituisce i caratteri della stringa in formato minuscolo
print(nome.lower())

## altro metodo molto interessante è replace(old, new)
## restituisce una nuova stringa dove tutte le occorrenze della sottostringa old sono rimpiazzate dalla sottostringa new
# esempio vogliamo rimuovere tutti i nomi Massimiliano e Roberto dalla stringa e rimpiazzarli con Max e Rob
text = "Massimiliano e Roberto sono due avvocati. Massimiliano ama Python. Roberto preferisce node"
text = text.replace('Massimiliano', 'Max')
text = text.replace('Roberto', 'Rob')

print(text)
```

*Et Voilà!*

![](/Users/Roberto/Documents/progetti/corso-informatica-avvocati/static/python/string_replace.png)

Per concludere la nostra lezione, indichiamo come poter dinamicamente inserire dati all'interno dello *script*, ossia l'istruzione `prompt(message)`

Attraverso l'istruzione input()` stiamo sostanzialmente chiedendo all'utente di inserire un *input* che può essere costituito da numeri, caratteri o da numeri e caratteri. Di *default* tutto è considerato come se fosse una **stringa**. Vediamo come possiamo utilizzarlo.

```python
# richiede i dati all'utente
nome = input('Inserisci il tuo nome:\n ')

# output
print('Ciao ' + nome + '!')
```

![](/Users/Roberto/Documents/progetti/corso-informatica-avvocati/static/python/input.png)

