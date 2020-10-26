# Programmare per il WEB

## HTML

### Introduzione all'HTML

**HTML** è l’acronimo di *HyperText Markup Language* (“Linguaggio di contrassegno per gli Ipertesti”) e non è un vero e proprio linguaggio di programmazione. Si tratta invece di un **linguaggio di markup** (di ‘contrassegno’ o ‘di marcatura’), che, sostanzialmente, descrive come disporre gli elementi all’interno di una pagina.

Quando navighiamo su qualunque pagina web, il nostro browser non fa altro che interpretare il contenuto HTML della pagina in questione al fine di visualizzare sullo schermo gli elementi della pagina, in conformità a quanto indicato nel testo HTML.

![](./static/html-1.png)

Come potete vedere in questo esempio, abbiamo due grandi riquadri:

1. il riquadro di sinistra contiene la rappresentazione della pagina in formato HTML;
2. il riquadro di destra contiene la rappresentazione effettiva della pagina sul nostro browser.

L'elemento caratteristico dell'HTML è costituito dall'utilizzo dei **tag** o **etichette**. Si tratta dei marcatori che andremo ad utilizzare per inserire gli elementi all'interno della pagina. Hanno la peculiarità di essere racchiusi tra parentesi angolari.

Per fare un esempio, il **tag** `<h1>` identifica il **Titolo 1** del nostro documento. Più precisamente, nella pagina sopra indicata, la sintassi corretta è `<h1>Hello World!</h1>`.Il senso è il seguente:

*Tutto ciò che è compreso tra il **tag** di apertura (<h1>) e quello di chiusura (</h1>) è rappresentato dall'elemento **Titolo 1**.* 

> La sintassi dei **tag** HTML è costituita da `<tag> contenuto </tag>. Ci sono però alcune eccezioni.

A questo punto, esaminiamo la pagina sopra riportata al fine di estrarre i relativi **tag**.

| Tag             | Descrizione                                                  |
| --------------- | ------------------------------------------------------------ |
| <!DOCTYPE html> | Serve semplicemente a comunicare al browser che il file è una pagina HTML redatta secondo lo standard HTML5. |
| <html>          | È il tag che racchiude tutta la pagina. Volendo, possiamo specificare la lingua della pagina, utilizzando l’attributo `lang="it"` |
| <head>          | Questo **tag** contiene una serie di informazioni utili per la gestione della pagina. Ad esempio può conterere il titolo che apparirà nei motori di ricerca e sulle etichette del browser (come abbiamo fatto utilizzando il tag <title> ). Solitamente in questa sezione si inseriscono le regole di stile e, a seconda dei casi, anche gli script di *javascript* |

Utilizzando i comuni browser è possibile sempre verificare il codice sorgente HTML di qualsiasi pagina web. Ad esempio, con **chrome** è sufficiente cliccare su un punto qualsiasi della pagina con il tasto destro e selezionare l'opzione: **ispeziona**.

Tra l'altro, nel momento in cui si utilizzano gli strumenti per sviluppatori di Chrome è anche possibile modificare in tempo reale l'aspetto della pagina.

![](./static/html-2.png)

Per fare ciò, è sufficiente accedere agli strumenti per sviluppatori, cliccare nel riquadro di sinistra sulla sintassi HTML della pagina e modificare il contenuto dei singoli elementi della pagina. 

### Elementi e TAG

Abbiamo, quindi, visto che in una pagina HTML tutti gli elementi sono rappresentati da **tag**. Queste etichette hanno la funzione di descrivere il tipo di elemento che poi sarà rappresentato nel browser. Tuttavia, sarebbe scorretto assegnare ai **tag** un ruolo meramente grafico o estetico. La principale funzione del **tag** è a livello semantico. Assegnare il **tag** <h1> invece del tag <h2> non ha, infatti, esclusivamente un risvolto grafico (che potrebbe essere modificato con il CSS), ma anche e, soprattutto, la funzione di specificare che si tratta di un **Titolo 1** piuttosto che di un **Titolo 2**.

Abbiamo già detto che, generalmente, la sintassi di un elemento HTML è la seguente: `<tag> contenuto </tag>`. In questo caso si parla di elementi **contenitori**. Il contenuto è delimitato, infatti, da:

- un **tag** di apertura (es. <h1>)
- un **tag** di chiusura (es. </h1>)

Tutto ciò che è compreso tra il **tag** di apertura e quello di chiusura è, infatti, il **contenuto** dell'elemento (es. il contenuto del **Titolo 1**, del **Titolo 2**, del semplice **paragrafo** e così via)

Torniamo all'esempio di prima che riproponiamo qui di seguito.

![](./static/html-1.png)

Possiamo notare che il nostro **Titolo 1** (*Hello World*) è, a sua volta, racchiuso da un elemento `<body> </body>` e, a sua volta, da un elemento `<html></html>`. Questo perché l'HTML è, sostanzialmente, come un grande **albero** dove i rami sono degli elementi **contenitori** e le estremità sono composte da **elementi non contenitori** come testi, immagini o caselle di input.

### Alcuni tipi di Elementi

| Tag                              | Descrizione                                                  |
| -------------------------------- | ------------------------------------------------------------ |
| da <h1> a <h6>                   | Sono i Titoli (ovviamente da Titolo 1 a Titolo 6)            |
| <p>                              | SI tratta del **paragrafo**. Al termine di ogni **paragrafo** si va a capo. Attenzione! Se inserisco due frasi all'interno di un elemento **paragrafo**, non andrò a capo neanche se digiterò il tasto INVIO. Per forzare l'interruzione di riga all'interno di un **paragrafo** si utilizza il **tag** `<br />` (*breakline*) |
| <b> o più correttamente <strong> | Si tratta del **grassetto** (*bold*) che rappresenta una cd. *strong emphasis* |
| <em>                             | Si tratta del **corsivo** (anche se più correttamente si riferisce non tanto allo stile, quando a concetti che vanno **enfatizzati**) |
| <ul> e <ol>                      | Si tratta, rispettivamente, della **lista non ordinata** e della lista **ordinata** |
| <li>                             | Si tratta del singolo elemento di una **lista ordinata** o di una **lista non ordinata** |

Proviamo a scrivere una pagina di esempio in cui ci presentiamo, utilizzando combinazioni di questi elementi.

<img src="./static/html-3.png" style="zoom:80%;" />

Commentiamo il codice sopra indicato:

- l'elemento <h1> </h1> racchiude il **Titolo 1** che non è stato modificato;
- l'elemento <p></p> racchiude del testo in cui abbiamo indicato alcune parole in **grassetto** (tag `<b> </b>`) ed altre in *corsivo* (tag `<em> </em>`);
- l'ulteriore elemento `<p></p>` racchiude del testo e un elenco puntato (`<ul> </ul>`) con tre elementi (`<li> </li>);
- infine abbiamo un ultimo elemento `<p></p>`.

A questo punto non resta che fare un po' di pratica!

### I commenti

I **commenti** in HTML, come in altri linguaggi (come poi vedremo), permettono di aggiungere alla pagina una serie di annotazioni che non incidono sulla sua visualizzazione. Hanno le seguenti funzioni: 

- Scrivere annotazioni generiche;
- Rendere inattive porzioni di codiceper effettuare dei test;
- Segnalare la chiusura di blocchi di codice per evitare confusione (specialmente in presenza di strutture molto annidate);

Il commento si inserisce utilizzando la seguente sintassi:

`<!-- COMMENTO -->`

![](./static/html-4.png)

### Le Tabelle

In HTML una **tabella** è delimitata dai **tag** `<table> </table>` ed ha la seguente composizione:

| Tag         | Descrizione                                                  |
| ----------- | ------------------------------------------------------------ |
| `<table>`   | Delimita l'intera tabella                                    |
| `<caption>` | Possiamo definirla come il titolo della tabella.             |
| `<tr>`      | Delimita una riga di una tabella                             |
| `<td>`      | Delimita una colonna di una tabella e contiene effettivamente i dati |
| `<th>`      | Delimita l'intestazione della tabella                        |

Riproduciamo quanto abbiamo scritto sopra.

![](./static/html-5.png)

Noterete l'utilizzo di alcuni **tag** come:

- `<code></code>` che si utilizza per identificare semanticamente porzioni di codice;
- `&lt` e `&gt` che rientrano nelle cd. **entità HTML**. Si utilizzano per rappresentare dei simbolli che potrebbero essere letti dal browser come delle entità HTML vere e proprie, quando, invece vogliamo solo inserirle come puro testo.

### I link

Elemento centrale del **web**, la possibilità di collegare pagine diverse (ma anche elementi diversi di una stessa pagina) è resa possibile dall'utilizzo del **tag** `<a> </a>`. La sintassi del **link** è la seguente:

- **tag** di apertura - `<a>`
- **attributo** `href` che contiene l'indirizzo della risorsa verso cui effettuare il collegamento;
- **attributo** `_target` (eventuale), si utilizza per far aprire una pagina diversa del browser (mediante il valore `_blank`)
- **contenuto** del link (ossia l'elemento su cui materialmente effettuare il *click*)
- **tag** di chiusura - `</a>`

Vediamo un semplice esempio.

![](./static/html-6.png)

### I Form

Per concludere la nostra breve panoramica sul linguaggio HTML, parliamo dei form che rappresentano l'elemento **principale** per raccogliere i dati dell'utente.

## CSS


## JAVASCRIPT