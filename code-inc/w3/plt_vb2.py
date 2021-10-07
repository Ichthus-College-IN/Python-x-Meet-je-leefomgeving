import numpy as np
import matplotlib.pyplot as plt

jaren = np.arange(1981, 2022)                         # bereik x-as
temp = np.sqrt(jaren) - 2*np.random.rand(len(jaren))  # meetpunten maken
trend = np.sqrt(jaren) - 1                            # trendlijn maken

plt.figure()                                          # figuur maken
plt.plot(jaren, temp,'k.', label='Meting')            # meetpunten plotten
plt.plot(jaren, trend, 'r-', label='Trend')           # trendlijn plotten
plt.xlabel('Jaren')                                   # x-as label
plt.ylabel('$T$ (graden Celsius)')                    # y-as label
plt.suptitle("Hoogst gemeten temperatuur in Madrid")  # titel
plt.legend()                                          # legenda
plt.grid()                                            # lijnen
plt.show()                                            # figuur weergeven