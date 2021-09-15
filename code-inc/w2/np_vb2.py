# We maken een test array om als voorbeeld te gebruiken.
test_array = np.arange(1,11)     # Ziet eruit als: [ 1 2 3 4 5 6 7 8 9 10 ]

# Wanneer we een enkel element willen selecteren kan dat als volgt:
element1 = test_array[0]         # Het eerste element heeft index '0'.
element7 = test_array[6]         # Dit heeft dus als resultaat '7'

# Wanneer we een deelverzameling willen selecteren
deel_array1  = test_array[2:5]    # Selecteer element 2 TOT 5 (t/m 4)
deel_array2  = test_array[2:-2]   # Selecteer van 2e t/m 2 na laatste
deel_array3  = test_array[:-2]    # Vanaf begin t/m twee na laatste
deel_array4  = test_array[2:]     # Vanaf tweede

# Een kopie maken is speciaal:
kopie_arr = test_array.copy()     # Twee verschillende arrays
same_arr  = test_array            # Twee namen voor hetzelfde array