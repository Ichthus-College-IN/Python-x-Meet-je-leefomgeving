import numpy as np

data = np.array([1,2,3,4,5,6]) # een test array

# Deze loop print elk element in data
for i in data:
    print(i)
    
# De volgende for-loop start pas bij een bepaalde index (2)
for i in range(2, len(data)):
    print(data[i])

# Een array kan ook uit twee dimensies bestaan.
# Dat houdt in dat bijvoorbeeld data[0] zelf ook meerdere waarden bevat:
data = np.array([[1,2,3], [3,4,5]])

print('data = ', data)
print('Gemiddelde van ALLE items = ', np.mean(data))

# Berekening van het gemiddelde van elk item apart kan met een for-loop:
for item in data:
    print('gemiddelde van', item, ' = ', np.mean(item)) 

# Je kunt ook het gemiddelde van een 'as' nemen:
print('Kolom gemiddeldes = ', np.mean(data, axis=0)) # y-as
print('Rij   gemiddeldes = ', np.mean(data, axis=1)) # x-as