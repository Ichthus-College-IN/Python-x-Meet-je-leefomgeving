# Begin met een subplots.
# sharex=True zorgt dat de x-as gedeeld wordt voor alle grafieken
# sharey=True idem voor de y-as
fig, axarr = plt.subplots(2, 2, sharex=True, sharey=True)

x = np.linspace(0,2*np.pi)                      # startwaarden

axarr[0,0].plot(x,np.cos(x)**2)                 # linksboven
axarr[0,1].plot(x,np.sin(x)**2)                 # rechtsboven
axarr[1,0].plot(x,np.cos(x)*np.sin(x))          # linksonder
axarr[1,1].plot(x,np.cos(x)**2*np.sin(x)**2)    # rechtsonder

fig.suptitle("Vier plotjes tegelijk")