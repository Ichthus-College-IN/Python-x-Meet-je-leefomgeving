import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(-2*np.pi, 2*np.pi, num=1001)
y = np.sin(x)
fig, ax = plt.subplots(figsize=[8,4])
ax.plot(x,y)
fig.savefig('sinus.png', dpi=300)
fig.savefig('sinus2.png', dpi=1200)