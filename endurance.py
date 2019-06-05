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
ore = int(tempo)
minuti = int((tempo - ore) * 60)
m = tempo - ore
mint = int (m * 60)
s =(m - mint) * 60

print("Durata volo: ", ore, "ore", mint, "minuti", s, "secondi")
 
