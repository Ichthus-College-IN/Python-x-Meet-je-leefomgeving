# Gebruik een testarray
test_array = np.arange(1,11)     # Ziet eruit als: [ 1 2 3 4 5 6 7 8 9 10 ]

# Berekening van minimum, etc.; let op de np. aan het begin
min_arr = np.min(test_array)      # Geeft minimum van array (1)
max_arr = np.max(test_array)      # Geeft maximum van array (10)
sum_arr = np.sum(test_array)      # Geeft som van array (55)
avg_arr = np.mean(test_array)     # Geeft gemiddelde van array (5.5)

# Eigenschappen van een array;
ta_lengte = len(test_array)     # Geeft aantal getallen in array (10,)
ta_dtype  = test_array.dtype    # Geeft datatype in array (int32)