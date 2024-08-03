import matplotlib.pyplot as plt
import numpy as np

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

def spiral_of_numbers(n_points):
    x = []
    y = []
    colors = []

    angle = 0
    step = 0.1
    for i in range(1, n_points + 1):
        angle += step
        r = angle
        x.append(r * np.cos(angle))
        y.append(r * np.sin(angle))
        if is_prime(i):
            colors.append('black')
        else:
            colors.append('gray')
    
    return x, y, colors

def plot_spiral(n_points):
    x, y, colors = spiral_of_numbers(n_points)
    
    plt.figure(figsize=(10, 10))
    plt.scatter(x, y, c=colors, s=10)
    plt.axis('equal')
    plt.axis('off')
    plt.show()

# Number of points to plot
n_points = 1000000
plot_spiral(n_points)
