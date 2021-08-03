import timeit

# De functie timeit heeft een input statement (stmt) nodig, een setup (setup), 
# en een aantal herhalingen (number)
# De output van de functie is dan de duur van het aantal herhalingen in seconden
# verstreken_tijd = timeit.timeit(stmt,setup,number=10000)

# De code van de setup wordt 1 keer, aan het begin, gerund en de code in de
# stmt wordt het aantal ingevoerde herhalingen gerunt.


# Het stmt staat geheel tussen ''' ''', en bevat alleen het aanroepen van de functie

# We doen niks met de output (return), slaan die niet op in een variabele.
stmt1 = '''
methode1(n)
'''
# De setup bevat eventuele initiele parameters en de definitie van de functie(s)
# Let op: de setup moet ook het importeren van benodigde packages bevatten.
setup1 = '''
import numpy as np

n = 100                                     # aantal random getallen
random_nrs = np.random.randint(100,size=n)  # n random int tussen 0 en 99

def methode1(n):
    even_nrs1 = []                          # maak lege lijst voor even getallen                 
    for element in random_nrs:              # loop door de hele lijst
        if element % 2 == 0:                # als een getal even is (% 2 = 0)
            even_nrs1.append(element)       # voeg het getal toe aan de lijst even_nrs1
    return even_nrs1
''' 
# Idem voor methode 2:
stmt2 = '''
methode2(n)
'''
setup2 = '''
import numpy as np

n = 100                                     # aantal random getallen
random_nrs = np.random.randint(100,size=n)  # n random int tussen 0 en 99

def methode2(n):
    masker_even_getallen = random_nrs % 2 == 0  # maak een masker voor even getallen
    even_nrs2 = random_nrs[masker_even_getallen] # gebruik het masker
    return even_nrs2
''' 

# Nu gaan we de snelheidsmeting uitvoeren
k = 10000
methode1_tijd = timeit.timeit(stmt1,setup1,number=k)
methode2_tijd = timeit.timeit(stmt2,setup2,number=k)

# En de resulaten printen
print(f'methode 1 duurt: {methode1_tijd:.4f} sec bij {k:.1e} herhalingen')
print(f'methode 2 duurt: {methode2_tijd:.4f} sec bij {k:.1e} herhalingen')