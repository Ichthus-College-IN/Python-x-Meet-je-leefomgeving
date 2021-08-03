# Gebruik een testarray
test_array = np.arange(1,11)     # Ziet eruit als: [ 1 2 3 4 5 6 7 8 9 10 ]

# Berekening van minimum, etc.; let op de verplichte () aan het eind
min_arr = test_array.min()      # Geeft minimum van array (1)
max_arr = test_array.max()      # Geeft maximum van array (10)
sum_arr = test_array.sum()      # Geeft som van array (55)
avg_arr = test_array.mean()     # Geeft gemiddelde van array (5.5)

# Eigenschappen van een array; let op het ontbreken van () aan het eind
ta_lengte = test_array.size     # Geeft aantal getallen in array (10,)
ta_dtype  = test_array.dtype    # Geeft datatype in array (int32)

# Deze manier van aanroepen "functie(argument)" is ook toegestaan
min_arr = np.min(test_array)    # Geeft minimum van array (1)