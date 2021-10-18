import numpy as np
import matplotlib.pyplot as plt

# Maak 2 arrays x en y, waarbij y = sin(x)
x = np.linspace(0,2*np.pi,num=100)
y = np.sin(x)             # Per element in x wordt sin(x) uitgerekend
fig, ax = plt.subplots()  # Maak een nieuw figuur
ax.plot(x,y)              # Plot punten (x,y)

fig, ax = plt.subplots()  # Maak een nieuw figuur
ax.plot(x,y**2)           # Plot punten (x,sin(x)^2)