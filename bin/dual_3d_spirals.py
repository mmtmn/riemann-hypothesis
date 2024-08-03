import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

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

def alternating_spiral_of_numbers_3d(n_points):
    x = []
    y = []
    z = []
    colors = []

    angle = 0
    step = 0.1
    z_step = 0.01
    for i in range(1, n_points + 1):
        angle += step
        r = angle
        if i % 2 == 0:
            # Spiral upwards
            x.append(r * np.cos(angle))
            y.append(r * np.sin(angle))
            z.append(i * z_step)
        else:
            # Spiral downwards
            x.append(r * np.cos(angle))
            y.append(r * np.sin(angle))
            z.append(-i * z_step)
        
        if is_prime(i):
            colors.append('black')
        else:
            colors.append('gray')
    
    return x, y, z, colors

def plot_alternating_spiral_3d(n_points):
    x, y, z, colors = alternating_spiral_of_numbers_3d(n_points)
    
    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(x, y, z, c=colors, s=10)
    ax.set_axis_off()
    plt.show()

# Number of points to plot
n_points = 1000000
plot_alternating_spiral_3d(n_points)
