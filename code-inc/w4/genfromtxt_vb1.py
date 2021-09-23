# de naam van het bestand
dir = 'https://github.com/Ichthus-College-IN/Python-x-Meet-je-leefomgeving/tree/main/code-inc/w4'
filename = dir+'vb1.txt'  # het 'optellen' van strings

# lees de data van dit komma-gescheiden bestand
data = np.genfromtxt(filename, delimiter=',')

# als het goed is kun je zien dat data een array met floats is
# en de size ervan is (20,3); zie de Variable explorer
# of bekijk het resultaat van onderstaande print
print('size of data = ', np.shape(data)) 

# plot de ingelezen data; kolom 0 wordt niet gebruikt
x = data[:,1]   # selecteer kolom 1
y = data[:,2]   # selecteer kolom 2
plt.plot(x,y)   # plot x en y

plt.show()