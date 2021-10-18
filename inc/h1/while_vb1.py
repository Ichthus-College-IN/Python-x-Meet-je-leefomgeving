v0 = 25   # beginsnelheid
g = 9.81  # zwaartekracht
t = 0.    # begintijd
dt = 0.25 # tijdstap
y = 0     # beginhoogte

# print en bereken de hoogte van een softbal
while y >= 0:
    print(t, y)
    
    y = v0*t - 0.5*g*t**2
    t = t + dt