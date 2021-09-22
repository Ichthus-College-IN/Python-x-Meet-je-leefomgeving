import numpy as np

samples = int(1e5)
L = np.random.normal(15.5,1.0,size=samples)
d = np.random.normal(35.0,5.0,size=samples)
R = np.random.normal(20.0,3.0,size=samples)
A = np.random.normal(2.20,1.3,size=samples)

for i in range(samples):
    if A[i] < 0:
        A[i] = 0
        
file = open("data_h4.txt", "w")
file.write("L,     d,     R,     A,     \n")

for i in range(samples):
    string = "{:.3f},{:.3f},{:.3f},{:.3f}\n".format(L[i], d[i], R[i], A[i])
    file.write(string)
    
file.close()