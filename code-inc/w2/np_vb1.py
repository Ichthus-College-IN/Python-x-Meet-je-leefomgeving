# De volgende voorbeelden leveren allemaal arrays op met ints:
array1a  = np.array([0,1,2,3,4,5]) # Vanuit een Python-lijst
array1b  = np.arange(6)            # Een bereik, beginnend bij 0
# Let op: het resultaat van beide arrays is hetzelfde, maar de tweede 
# functie kost minder typwerk, zeker bij een groter bereik.

## De volgende voorbeelden leveren allemaal arrays met floats op:
nullen   = np.zeros(6)             # Array gevuld met 6 nullen (float)
enen     = np.ones(6)              # Array gevuld met 6 enen   (float)
random   = np.random.rand(6)       # Array gevuld met 6 random getallen
                                   # tussen de 0 en 1

# Om een array te maken met allemaal stapjes tussen twee waarden (grid)
# kunnen deze functies gebruikt worden:
grid1 = np.arange(0.,5.,0.25)      # 0 TOT 5 met stapjes van 0.25
grid2 = np.linspace(0.,5.,num=20)  # 0 TOT EN MET 5, 20 gelijke afstanden