rispostecorrette = 0
numerodirisposte = 4
risposta1 = input("quale articolo disciplina la nullità del contratto?\n")
if risposta1 == "1418":
print ("la risposta è corretta")
rispostecorrette = rispostecorrette + 1
else:
print ("la risposta è sbagliata")
risposta2 = input("quale articolo disciplina la responsabilità extracontrattuale?\n")
if risposta2 == "2043":
print ("la risposta è corretta")
rispostecorrette = rispostecorrette + 1
else:
print ("la risposta è sbagliata")
risposta3 = input("quale articolo della Costituzione disciplina la libertà di manifestazione del pensiero?\n")
if risposta3 == "21":
print ("la risposta è corretta")
rispostecorrette = rispostecorrette + 1
else:
print ("la risposta è sbagliata")
risposta4 = input("quale articolo della Costituzione disciplina il procedimento di revisione costituzionale?\n")
if risposta4 == "138":
print("la risposta è corretta")
rispostecorrette = rispostecorrette + 1
else:
print("la risposta è sbagliata")
voto = int ((rispostecorrette*30)/numerodirisposte)
if voto >= 18:
print("l'esame è superato con voto " + str(voto))
else:
print("torna alla prossima sessione")
