import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

nx = 150
ny = 50

fig = plt.figure("12")
data = np.zeros((nx, ny))
data = data+1
# im = plt.imshow(data, cmap='gist_gray_r', vmin=0, vmax=1)
# im = plt.imshow(data)
plt.imshow(data)


# def init():
#     im.set_data(np.zeros((nx, ny)))

# def animate(i):
#     xi = i // ny
#     yi = i % ny
#     data[xi, yi] = 1
#     im.set_data(data)
#     return im

# anim = animation.FuncAnimation(fig, animate, init_func=init, frames=nx * ny,interval=50)