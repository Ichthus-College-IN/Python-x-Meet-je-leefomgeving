"""  Data wegschrijven in een bestand inclusief een header
"""
import numpy as np

# Specificeren van object in Python dat het nieuwe bestand aanwijst
# 'w' staat voor 'write' en geeft aan dat in het bestand geschreven mag worden 
file = open('vb1.txt', 'w')

# Aanmaken van numpy arrays om weg te schrijven naar bestand
x = np.linspace(-2*np.pi, 2*np.pi, num=20)
y = np.sin(x)

# Metadata
col0 =  '     i'  # een onbelangrijke string; alleen voor leesbaarheid
col1 =  '      x' # een onbelangrijke string; alleen voor leesbaarheid
col2 =  ' sin(x)' # een onbelangrijke string; alleen voor leesbaarheid
par1 = 50         # een waarde / parameter 1
par2 = 0.12       # een waarde / parameter 2

# Schrijven van header, herkenbaar aan # op eerste positie van elke regel
file.write('# Dit is de header (eerste regel) \n')
file.write('# Schaal parameter horizontaal:\t {:5.2f}\n'.format(par1))
file.write('# Schaal parameter verticaal  :\t {:5.2f}\n'.format(par2))
file.write('#{:s} \t {:s} \t {:s}\n'.format(col0, col1, col2))
# de opgegeven namen worden weggeschreven als een character-string met
# daartussen steeds een \t (tab) voorafgegaan/gevolgd door een spatie

# Schrijven van (meet)gegevens:
for i in range(len(x)):
   file.write('{:7d} \t {:7.4f} \t {:7.4f} \n'.format(i, x[i], y[i]))
# op iedere regel staat nu: een geheel getal op de eerste 7 posities, 
# spatie, tab, spatie, decimaal getal met 4 decimalen op 7 posities, 
# spatie, tab, spatie, decimaal getal met 4 decimalen op 7 posities,    
# spatie, en de regel wordt afgesloten met een \n (new-line symbool).
# MERK OP: de laatste  regel is een lege regel.
   
file.close()