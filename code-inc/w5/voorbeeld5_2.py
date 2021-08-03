# Rechte lijn
def f(x,a,b):
    return a + b*x

# Sinus
def g(x,a,b,c):
    return a + b*np.sin(c*x)

## Simpele plotfunctie:
# plot "functie" op het bereik "x"
# extra argumenten worden doorgegeven met *args
def my_plot(x,functie,*args):
    plt.plot(x,functie(x,*args))
    plt.show()
    
# Bereik:
x_arr = np.linspace(-5.,5., num=100)