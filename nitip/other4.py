import numpy as np
import matplotlib.pyplot as plt

# Generate some data
nrows, ncols = 1000, 1000
xmin, xmax = -32.4, 42.0
ymin, ymax = 78.9, 101.3

dx = (xmax - xmin) / (ncols - 1)
dy = (ymax - ymin) / (ncols - 1)

x = np.linspace(xmin, xmax, ncols)
y = np.linspace(ymin, ymax, nrows)
x, y = np.meshgrid(x, y)

z = np.hypot(x - x.mean(), y - y.mean())
x, y, z = [item.flatten() for item in (x,y,z)]

# Scramble the order of the points so that we can't just simply reshape z
indicies = np.arange(x.size)
np.random.shuffle(indicies)
x, y, z = [item[indicies] for item in (x, y, z)]

# Up until now we've just been generating data...
# Now, x, y, and z probably represent something like you have.

# We need to make a regular grid out of our shuffled x, y, z indicies.
# To do this, we have to know the cellsize (dx & dy) that the grid is on and
# the number of rows and columns in the grid.

# First we convert our x and y positions to indicies...
idx = np.round((x - x.min()) / dx).astype(np.int)
idy = np.round((y - y.min()) / dy).astype(np.int)

# Then we make an empty 2D grid...
grid = np.zeros((nrows, ncols), dtype=np.float)

# Then we fill the grid with our values:
grid[idy, idx] = z

# And now we plot it:
plt.imshow(grid, interpolation='nearest',
        extent=(x.min(), x.max(), y.max(), y.min()))
plt.colorbar()
plt.show()
