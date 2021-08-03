'''
Voorbeeld: het gebruik van genfromtxt
'''
import numpy as np
import matplotlib.pyplot as plt

# de naam van het bestand
dir = 'http://nspracticum.science.uu.nl/DATA2020/DATA-Py/Databestanden/'
filename = dir+'vb1.txt'  # het 'optellen' van strings

# lees de data in dit tab-gescheiden bestand
data = np.genfromtxt(filename, delimiter='\t')

# als het goed is kun je zien dat data een array met floats is
# en de size ervan is (20,3); zie in Spyder bij je Variable explorer
# of bekijk het resultaat van onderstaande print
print('size of data = ', np.shape(data)) 

# plot de ingelezen data; kolom 0 wordt niet gebruikt
(x, y) = (data[:,1], data[:,2])
plt.plot(x,y)

plt.show()