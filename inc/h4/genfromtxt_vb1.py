import numpy as np

# de naam van het bestand
file = 'vb1.txt'

# lees de data van dit komma-gescheiden bestand
data = np.genfromtxt(file, delimiter=',')

# als het goed is kun je zien dat data een array met floats is
# en de size ervan is (20,3); zie de Variable explorer
# of bekijk het resultaat van onderstaande print
print('size of data = ', np.shape(data)) 

# plot de ingelezen data; kolom 0 wordt niet gebruikt
x = data[:,1]   # selecteer kolom 1
y = data[:,2]   # selecteer kolom 2