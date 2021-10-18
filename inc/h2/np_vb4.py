# Gebruik van een test_array
test_array = np.array([12, 1, 7, 8, 4, 3])
print(" test_array (origineel) = ", test_array)

# Aanmaken van een masker met de voorwaarde dat elementen > 5 moeten zijn
masker = test_array > 5     # True als element > 5, anders False
print(" masker =                 ", masker)                                         

# Selecteren van elementen waarvoor het masker True is
g5 = test_array[masker]     # Met de blokhaken [] gebruik je het masker
print(" Elementen die > 5 zijn:  ", g5)

# Aanpassen van de waarde van alle elementen waarvoor het masker True is
test_array[masker] = 0      # Zet alle elementen >5 gelijk aan 0
print(" test_array (nieuw)     = ", test_array)                                         