import matplotlib.pyplot as plt
import numpy as np

points = 60*24
base_temp = 15*np.ones(points)
domain_curve = np.linspace(0,np.pi,points)
curve = np.sin(domain_curve)**2

data = np.array([])
for i in range(4,8):
    domain_fourier = np.linspace(0,i*np.pi,points)
    fourier = np.cos(domain_fourier / 2)
    randomizer = np.random.uniform(3,5,points)
    temp = base_temp + (randomizer + fourier)*curve
    data = np.append(data, temp)
    plt.plot(domain_curve,temp)
    
data = data.reshape(points,4)

final_data = np.empty([1,2])
for i in range(points):
    stations = np.array([0,1,2,3])
    np.random.shuffle(stations)
    values = np.vstack((stations+1, (data[i])[stations])).T
    final_data = np.concatenate((final_data,values),axis=0)
    
final_data = final_data[1:]

np.savetxt("data_h4.txt", final_data, delimiter=",")