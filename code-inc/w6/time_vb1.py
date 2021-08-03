# vind alle even getallen uit een random lijst op twee manieren
import numpy as np
import time

n = 1000000                                   # aantal random getallen
random_nrs = np.random.randint(100,size=n)  # n random int tussen 0 en 99

start_tijd1 = time.time()                   # start de tijd voor methode 1
even_nrs1 = []                              # maak lege lijst voor even getallen                 
for element in random_nrs:                  # loop door de hele lijst
    if element % 2 == 0:                    # als een getal even is (% 2 = 0)
        even_nrs1.append(element)           # voeg het getal toe aan de lijst even_nrs1
eind_tijd1 = time.time()                    # stop de tijd voor methode 1
verstreken_tijd1 = eind_tijd1-start_tijd1   # bereken de verstreken tijd
print(f'methode 1 duurt: {verstreken_tijd1:.4f} sec')

start_tijd2 = time.time()                   # start de tijd voor methode 2
masker_even_getallen = random_nrs % 2 == 0  # maak een masker voor even getallen
even_nrs2 = random_nrs[masker_even_getallen] # gebruik het masker
eind_tijd2 = time.time()                    # stop de tijd voor methode 2
verstreken_tijd2 = eind_tijd2-start_tijd2   # bereken de verstreken tijd
print(f'methode 2 duurt: {verstreken_tijd2:.4f} sec')