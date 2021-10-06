import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(-2*np.pi, 2*np.pi, num=1001)
y = np.sin(x)
plt.figure(figsize=[8,4])
plt.plot(x,y)
plt.savefig('sinus.png', dpi=300)
plt.savefig('sinus2.png', dpi=1200)