import numpy as np
from matplotlib import cm
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.axes3d import Axes3D

x = np.arange(0,5,1)
y = np.arange(0,5,1)

xs, ys = np.meshgrid(x, y)
# z = calculate_R(xs, ys)
zs = xs**2 + ys**2

print('x: ',x)
print('y: ',y)
print('xs: ',xs)
print('ys: ',ys)
print('zs: ',zs)

zz = np.array([
    [0,0,0,0,0],
    [0,10,10,10,0],
    [0,20,20,20,0],
    [0,50,50,50,0],
    [0,0,0,0,0],])

fig = plt.figure()
ax = Axes3D(fig)
ax.plot_surface(xs, ys, zz, rstride=1, cstride=1, cmap=cm.coolwarm)
plt.show()
