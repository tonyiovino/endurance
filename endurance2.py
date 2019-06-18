quantita_str = input("Inserite la quantità in galloni del carburante: ")
quantita = float(quantita_str)

consumo_orario_str = input("Inserite il consumo orario: ")
consumo_orario = float(consumo_orario_str)

if quantita <= 0:
	print("La quantità del carburante deve essere maggiore di 0.")
elif consumo_orario <= 0:
	print("Il consumo deve essere maggiore di 0.")
else:
	tempo = quantita / consumo_orario

	ore = int(tempo)

	tempo = tempo - ore
	tempo = tempo * 60
	minuti = int(tempo)

	tempo = tempo - minuti
	tempo = tempo * 60
	secondi = int(tempo)

	print("Tempo in volo: ", ore, "h", minuti, "m", secondi, "s")

