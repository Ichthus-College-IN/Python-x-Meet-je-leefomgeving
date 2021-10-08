import numpy as np
import matplotlib.pyplot as plt

jaren = np.arange(1981, 2022)                         # bereik x-as
temp = np.sqrt(jaren) - 2*np.random.rand(len(jaren))  # meetpunten maken
trend = np.sqrt(jaren) - 1                            # trendlijn maken

fig, ax = plt.subplots()                              # figuur maken
ax.plot(jaren, temp, 'k.')            # meetpunten plotten
ax.plot(jaren, trend, 'r-')           # trendlijn plotten