#%% importeer de nodige modules
import numpy as np
import matplotlib.pyplot as plt

#%%
# Maak 2 arrays x en y, waarbij y = sin(x)
x = np.linspace(0,2*np.pi,num=100)
y = np.sin(x)              # Per element in x wordt sin(x) uitgerekend
plt.figure()               # Maak een nieuw figuur
plt.plot(x,y)              # Plot punten (x,y)

plt.figure()               # Maak een nieuw figuur
plt.plot(x,y**2)           # Plot sin(x)^2