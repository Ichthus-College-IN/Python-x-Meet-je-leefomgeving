import numpy as np
# Gebruik van ravel, reshape en T (=transpose/spiegelen)
a = np.array([[1,3,5], [2,4,6]])
at = a.T                          #  = [[1,2], [3,4], [5,6]]
b = a.ravel()                     #  = [1,3,5,2,4,6]
c = a.T.ravel()                   #  = [1,2,3,4,5,6]
a2 = c.reshape(2,3)               #  = [[1,2,3], [4,5,6]]