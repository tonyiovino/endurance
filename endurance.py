print("Inserisci la quantità di carburante: ")
quantità = -1
while quantità < 0:
	q_str = input()
	quantità=float(q_str)

print("Inserisci il consumo orario di carburante: ")
consumo = -1
while consumo < 0:
	c_str = input()
	consumo = float(c_str)

tempo = quantità / consumo

print("Il tempo di volo è ", tempo)

 