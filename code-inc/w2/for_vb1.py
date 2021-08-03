import numpy as np

data = np.array([[1,2,3], [3,4,5]])
print('data = ', data)
print('Gemiddelde van ALLE items = ', np.mean(data))

# Berekening van het gemiddelde van elk item apart gaat met een for-loop:
for item in data:
    print('gemiddelde van', item, ' = ', np.mean(item)) 
    
# De volgende for-loop doet hetzelfde maar is wat omslachtiger    
for i in range(len(data)):
    print('gemiddelde van data[', i, ']  = ', np.mean(data[i]))

# Als je data eenmaal in een array staat heb je geen for-loops nodig:     
print('Kolom gemiddeldes = ', np.mean(data, axis=0))
print('Rij   gemiddeldes = ', np.mean(data, axis=1))

data2 = np.array([1,2,3,4,5,6]) # tweede test array

# De volgende for-loop start pas bij een bepaalde waarde (2)
for i in range(2, len(data)):
    print(data[i])