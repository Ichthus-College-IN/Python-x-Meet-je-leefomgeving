import numpy as np

## Maak 3 arrays
a  = np.arange(25).reshape(5,5)  # een 5 bij 5 matrix
b1 = np.arange(10).reshape(2,5)  # een 2 bij 5 matrix
b2 = b1.T                        # een 5 bij 2 matrix

# Dit gaat goed:
conc1 = np.concatenate((a,b1))

# Dit gaat mis, niet matchende dimensies
conc2 = np.concatenate((a,b2))

# Met axis keyword wordt langs de tweede as gewerkt en lukt het wel
conc3 = np.concatenate((a,b2),axis=1)
# let op: python begint bij 0 met tellen, dus axis=1 is de tweede as
