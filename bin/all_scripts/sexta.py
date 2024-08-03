import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from collections import deque

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def sixteen_spirals_of_numbers_3d(n_points, step=0.1, z_step=1):
    x = []
    y = []
    z = []
    colors = []

    directions = deque([
        (1, 0, 0),   # +x axis
        (-1, 0, 0),  # -x axis
        (0, 1, 0),   # +y axis
        (0, -1, 0),  # -y axis
        (0, 0, 1),   # +z axis
        (0, 0, -1),  # -z axis
        (1, 1, 0),   # +x +y
        (-1, -1, 0), # -x -y
        (1, 0, 1),   # +x +z
        (-1, 0, -1), # -x -z
        (0, 1, 1),   # +y +z
        (0, -1, -1), # -y -z
        (1, 1, 1),   # +x +y +z
        (-1, -1, -1),# -x -y -z
        (1, -1, 1),  # +x -y +z
        (-1, 1, -1)  # -x +y -z
    ])

    angle = 0
    for i in range(1, n_points + 1):
        angle += step
        r = angle
        dx, dy, dz = directions[0]  # Get the current direction from the queue
        directions.rotate(-1)  # Rotate the queue to cycle through directions

        # Calculate the normalized factor for the direction
        norm_factor = np.sqrt(dx**2 + dy**2 + dz**2)
        norm_dx = dx / norm_factor
        norm_dy = dy / norm_factor
        norm_dz = dz / norm_factor

        # Calculate the spiral coordinates
        x_coord = r * norm_dx * np.cos(angle) - r * norm_dy * np.sin(angle)
        y_coord = r * norm_dy * np.cos(angle) + r * norm_dx * np.sin(angle)
        z_coord = r * norm_dz * np.cos(angle) if norm_dz != 0 else r * np.sin(angle)

        x.append(x_coord)
        y.append(y_coord)
        z.append(z_coord)
        
        if is_prime(i):
            colors.append('black')
        else:
            colors.append('gray')
    
    return x, y, z, colors

def plot_sixteen_spirals_3d(n_points, step=0.1, z_step=1):
    x, y, z, colors = sixteen_spirals_of_numbers_3d(n_points, step, z_step)
    
    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(x, y, z, c=colors, s=10)
    ax.set_axis_off()
    plt.show()

# Number of points to plot
n_points = 10000
# Adjust these parameters to increase outward spread
step = 0.1
z_step = 1
plot_sixteen_spirals_3d(n_points, step, z_step)
