## Simpele plotfunctie:
# plot een rechte lijn op het bereik "x"
# voor een grid maken we gebruik van een defaultwaarde
def my_plot(x,a,b,grid=True):
    y = a + b*x
    plt.plot(x,y)
    if grid:            # dit is hetzelfde als: if grid == True
        plt.grid()
    plt.show()
    
# Bereik:
x_arr = np.linspace(-5.,5., num=100)