fig, ax = plt.subplots()

## Simpele plotfunctie: plot een rechte lijn op het bereik "x"
# voor een grid maken we gebruik van een defaultwaarde
def mijn_plot(x,a,b,grid=True):
    y = a + b*x
    ax.plot(x,y)
    if grid == True:
        ax.grid()
    
x_arr = np.linspace(-5.,5., num=100)    # bereik x-as