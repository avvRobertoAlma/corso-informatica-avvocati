# la funzione accetta un solo parametro (rubrica_da_iterare)
def itera_rubrica(rubrica_da_iterare):
    for elemento in rubrica_da_iterare:
        for key in elemento:
            print(f"{key} : {elemento[key]}")

# rubrica stato iniziale
rubrica = [
    {
        "nome":"Roberto",
        "cognome":"Rossi",
        "email":"roberto.rossi@pec.it",
        "telefono":"340340000"
    },
    {
        "nome":"Mario",
        "cognome":"Rossi",
        "email":"Mario.rossi@pec.it",
        "telefono":"340340001"
    }
]

itera_rubrica(rubrica)
      
## aggiungiamo un elemento alla lista con il noto metodo .append()
rubrica.append({

        "nome":"Luca",
        "cognome":"Verdi",
        "email":"luca.verdi@pec.it",
        "telefono":"340340003"
    })



itera_rubrica(rubrica)