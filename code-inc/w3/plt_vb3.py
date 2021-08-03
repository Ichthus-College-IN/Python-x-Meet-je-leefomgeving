# Begin met een subplots.
# fig bevat de informatie van de gehele figuur.
# ax1 t/m ax3 bevatten informatie over de individuele plots.
# sharex en sharey zorgen ervoor dat zowel x- als y-as gedeeld zijn.
fig, (ax1, ax2, ax3) = plt.subplots(3, sharex=True, sharey=True)

x = np.linspace(0,2*np.pi)      # startwaarden

ax1.plot(x,np.cos(x)**2)        # plot sin(x)^2 in het eerste figuur
ax2.plot(x,np.sin(x)**2)        # plot cos(x)^2 in het tweede figuur
ax3.plot(x,np.cos(x)*np.sin(x)) # plot sin(x)*cos(x) in het derde figuur
ax1.grid()                      # lijnen toevoegen in het eerste plaatje

# suptitle verwijst naar de titel van de gehele figuur. Dit is dus een 
# eigenschap van de totale figuur f.
fig.suptitle("Drie plotjes tegelijk")
plt.show()