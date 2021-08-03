# Begin met een subplots.
# sharex='col' zorgt dat de x-coordinaat gedeeld wordt over de kolommen
# sharey='row' idem voor rijen en de y-coordinaat
fig, axarr = plt.subplots(2, 2, sharex='col', sharey='row')

x = np.linspace(0,2*np.pi)                      # startwaarden

axarr[0,0].plot(x,np.cos(x)**2)                 # linksboven
axarr[0,1].plot(x,np.sin(x)**2)                 # rechtsboven
axarr[1,0].plot(x,np.cos(x)*np.sin(x))          # linksonder
axarr[1,1].plot(x,np.cos(x)**2*np.sin(x)**2)    # rechtsonder

# suptitle verwijst naar de titel van de gehele figuur. Dit is dus een 
# eigenschap van de totale figuur fig.
fig.suptitle("Vier plotjes tegelijk")
plt.show()