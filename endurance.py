print("Inserisci la quantità di carburante: ")
quantita = -1
while quantita < 0:
	q_str = input()
	quantita=float(q_str)

print("Inserisci il consumo orario di carburante: ")
consumo = -1
while consumo < 0:
	c_str = input()
	consumo = float(c_str)

tempo = quantita / consumo

print("Il tempo di volo è ", tempo)

 
