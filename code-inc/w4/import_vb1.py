"""
Script om alle items in een bestand als string te interpreteren
Zo'n string bevat geen spaties of tab's.
Maak zelf je eigen oefen-bestand aan.
"""
f =  open("oefening.txt", "r")
block = f.readlines()

data = []   #  een lege Python lijst
for line in block:
    data.append( line.split() )  
# check data na runnen script