import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

a = np.array([[1, 2, 4], [5, 8, 7]], dtype = 'float') 
b = np.zeros((120,1))
b = b+12

fig = plt.figure("this new plot")

for d in range(12):
    print(d)
    plt.plot(a+d)
    plt.show()