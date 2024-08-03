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

def eight_spirals_of_numbers_3d(n_points, step=0.1, z_step=1):
    x = []
    y = []
    z = []
    colors = []

    angle = 0
    for i in range(1, n_points + 1):
        angle += step
        r = angle
        if i % 8 == 0:
            # Spiral along +z axis
            x.append(r * np.cos(angle))
            y.append(r * np.sin(angle))
            z.append(i * z_step)
        elif i % 8 == 1:
            # Spiral along -z axis
            x.append(r * np.cos(angle))
            y.append(r * np.sin(angle))
            z.append(-i * z_step)
        elif i % 8 == 2:
            # Spiral along +y axis
            x.append(r * np.cos(angle))
            y.append(i * z_step)
            z.append(r * np.sin(angle))
        elif i % 8 == 3:
            # Spiral along -y axis
            x.append(r * np.cos(angle))
            y.append(-i * z_step)
            z.append(r * np.sin(angle))
        elif i % 8 == 4:
            # Spiral along +x axis
            x.append(i * z_step)
            y.append(r * np.sin(angle))
            z.append(r * np.cos(angle))
        elif i % 8 == 5:
            # Spiral along -x axis
            x.append(-i * z_step)
            y.append(r * np.sin(angle))
            z.append(r * np.cos(angle))
        elif i % 8 == 6:
            # Spiral along +z axis, inverted
            x.append(-r * np.cos(angle))
            y.append(-r * np.sin(angle))
            z.append(i * z_step)
        else:
            # Spiral along -z axis, inverted
            x.append(-r * np.cos(angle))
            y.append(-r * np.sin(angle))
            z.append(-i * z_step)
        
        if is_prime(i):
            colors.append('black')
        else:
            colors.append('gray')
    
    return x, y, z, colors

def plot_eight_spirals_3d(n_points, step=0.1, z_step=1):
    x, y, z, colors = eight_spirals_of_numbers_3d(n_points, step, z_step)
    
    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(x, y, z, c=colors, s=10)
    ax.set_axis_off()
    plt.show()

# Number of points to plot
n_points = 100000
# Adjust these parameters to increase outward spread
step = 0.1
z_step = 1
plot_eight_spirals_3d(n_points, step, z_step)
