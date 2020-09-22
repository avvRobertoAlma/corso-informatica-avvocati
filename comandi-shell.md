# Introduzione ai comandi da shell

## La Shell

Che cos'è la *shell*?. Il termine *shell* significa letteralmente *guscio* e possiamo definirla come l'interfaccia tra l'utente e il sistema operativo.

Nei sistemi *UNIX*, specialmente lato *server*, è fondamentale imparare come gestire un sistema tramite interfaccia a linea di comando (in luogo della più intuitiva interfaccia grafica o GUI).

Da un punto di vista semplicistico la *shell* è un programma e come tale deve essere eseguito. Al riguardo, ci sono due possibilità:

- esecuzione di una *shell* tramite interfaccia grafica avviando il cd. *terminal*;
- esecuzione di una *shell* direttamente da linea di comando (tipicamente ciò avviene nell'ambito di una procedura di autenticazione ad un server remoto via *SSH*).

Ci sono ovviamente varie tipologie di *shell*, la più famosa delle quali è la *shell BASH* (Bourne Again Shell).

## Esecuzione di programmi nella shell

### Introduzione

Nei sistemi Linux, i programmi eseguibili vengono solitamente salvati in alcune cartelle come `/bin`, `/usr/bin` e `/usr/local/bin`. Se un programma è salvato in una di queste cartelle, può essere eseguito all'interno di una *shell*, semplicemente digitando il nome e premendo INVIO.

Ad esempio, il comando `ls` che restituisce, come output, la lista dei file e delle cartelle contenuti in una cartella, come da immagine che segue

![](./static/ls.png)

> La lista delle cartelle all'interno delle quali la *shell* ricercherà i comandi da eseguire è solitamente contenuta nella variabile `$PATH`

### Argomenti

Molti programmi accettano **argomenti** che possono essere altri comandi o più semplicemente codici che seguono il nome del programma.

Ad esempio, il comando `cat` è in grado di stampare all'interno del terminale il contenuto di un file di testo. 

Quale file di testo?

Esattamente il file di testo che è indicato come **argomento** del comando.

Un semplice esempio chiarisce la tematica.
```
$ cat a.txt
Questo è il contenuto di a.txt
```

Il comando come abbiamo visto visualizza a video il contenuto del file di testo.

> **Attenzione!**. Se il file di testo non si trova nella stessa cartella di lavoro, il comando restituirà un errore. Nel qual caso si dovrà indicare il percorso completo del file.

## Lista dei comandi principali

### Gestione dei file

#### Ottenere la lista dei file e delle cartelle

Si utilizza il comando `ls` già visto sopra. Di seguito una lista delle opzioni più comuni.

| Opzione | Descrizione |
| --- | --- |
| `--all` o `-a` | Normalmente `ls` omette i file nascosti (ossia quelli preceduti dal carattere `.`. L'aggiunta dell'opzione in questione consente la visualizzazione a video del nome dei file nascosti contenuti nella cartella di lavoro |
| `-l` | Visualizza ulteriori informazioni sui file (come i permessi, le dimensioni e la data di creazione) |
| `--recursive` o `-r` | Visualizza i contenuti della cartella in modo ricorsivo. Ciò significa che se la cartella contiene altre sottocartelle, saranno visualizzati anche tutti i file contenuti nelle sottocartelle e così via |

### Modifica della cartella di lavoro

Si utilizza il comando `cd` seguito dal percorso della cartella che si vuole utilizzare come cartella di lavoro.

Esempio: 

```
cd Documenti/pippo
```
Modifica la cartella di lavoro, da quella corrente a `./Documenti/pippo` 

> Importante è comprendere la struttura dei percorsi.
> 
> Un percorso `assoluto` è un percorso che è relativo alla cartella origine (ossia la cartella `/` )
> 
> Un percorso `relativo` è un percorso relativo alla cartella corrente.
> 
> Ad esempio se mi trovo nella cartella `Documenti/clienti` e voglio accedere a `Documenti/clienti/pippo` potrò semplicemente digitare `cd pippo`. In questo caso sto utilizzando un percorso relativo.

### Creazione di file

