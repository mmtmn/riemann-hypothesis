import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

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

def dual_spiral(n_points):
    x_up = []
    y_up = []
    z_up = []
    colors_up = []

    x_down = []
    y_down = []
    z_down = []
    colors_down = []

    angle = 0
    step = 0.1
    z_step = 0.01
    for i in range(1, n_points + 1):
        angle += step
        r = angle
        if i % 2 == 0:
            # Upward spiral
            x_up.append(r * np.cos(angle))
            y_up.append(r * np.sin(angle))
            z_up.append(i * z_step)
            if is_prime(i):
                colors_up.append('black')
            else:
                colors_up.append('gray')
        else:
            # Downward spiral
            x_down.append(r * np.cos(angle))
            y_down.append(r * np.sin(angle))
            z_down.append(-i * z_step)
            if is_prime(i):
                colors_down.append('black')
            else:
                colors_down.append('gray')
    
    return (x_up, y_up, z_up, colors_up), (x_down, y_down, z_down, colors_down)

fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection='3d')

spiral_data = []

def animate(i):
    ax.clear()
    if i < len(spiral_data):
        (x_up, y_up, z_up, colors_up, x_down, y_down, z_down, colors_down, title) = spiral_data[i]
        ax.scatter(x_up, y_up, z_up, c=colors_up, s=10)
        ax.scatter(x_down, y_down, z_down, c=colors_down, s=10)
        ax.set_title(title)
        ax.set_axis_off()

def recursive_spiral_plotting(n_points, depth=1):
    (x_up, y_up, z_up, colors_up), (x_down, y_down, z_down, colors_down) = dual_spiral(n_points)
    spiral_data.append((x_up, y_up, z_up, colors_up, x_down, y_down, z_down, colors_down, f'Spiral with {n_points} Points (Depth {depth})'))
    
    if len(x_down) <= 2:
        return

    # Further divide the downward spiral into new upward and downward spirals
    new_x_up = []
    new_y_up = []
    new_z_up = []
    new_colors_up = []

    new_x_down = []
    new_y_down = []
    new_z_down = []
    new_colors_down = []

    angle = 0
    step = 0.1
    z_step = 0.01
    for i in range(1, len(x_down) + 1):
        angle += step
        r = angle
        if i % 2 == 0:
            # New upward spiral
            new_x_up.append(r * np.cos(angle))
            new_y_up.append(r * np.sin(angle))
            new_z_up.append(i * z_step)
            if is_prime(i):
                new_colors_up.append('black')
            else:
                new_colors_up.append('gray')
        else:
            # New downward spiral
            new_x_down.append(r * np.cos(angle))
            new_y_down.append(r * np.sin(angle))
            new_z_down.append(-i * z_step)
            if is_prime(i):
                new_colors_down.append('black')
            else:
                new_colors_down.append('gray')

    spiral_data.append((new_x_up, new_y_up, new_z_up, new_colors_up, new_x_down, new_y_down, new_z_down, new_colors_down, f'New Spiral with {len(new_x_up) + len(new_x_down)} Points (Depth {depth + 1})'))

    # Recursively analyze the new downward spiral
    recursive_spiral_plotting(len(new_x_down), depth + 1)

# Number of points to plot
n_points = 100000
recursive_spiral_plotting(n_points)

ani = FuncAnimation(fig, animate, frames=len(spiral_data), interval=1000, repeat=False)
plt.show()
