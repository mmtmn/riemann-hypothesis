import numpy as np
import matplotlib.pyplot as plt
from mpmath import mp, zeta, mpc

# Set high precision
mp.dps = 50

# Function to calculate zeta function values on the critical line
def zeta_values_on_critical_line(t_start, t_end, num_points=10000):
    ts = np.linspace(t_start, t_end, num_points)
    zeta_vals = [zeta(mpc(0.5, t)) for t in ts]
    return ts, zeta_vals

# Function to calculate and visualize alternating buckets
def visualize_alternating_buckets(t_start, t_end, num_points=10000, bucket_size=100):
    ts, zeta_vals = zeta_values_on_critical_line(t_start, t_end, num_points)
    bucketed_zeros = []

    for i in range(0, len(ts), bucket_size):
        bucket = zeta_vals[i:i+bucket_size]
        bucketed_zeros.append(sum(abs(z) < 1e-10 for z in bucket))

    plt.plot(range(len(bucketed_zeros)), bucketed_zeros, label="Zeros in Buckets")
    plt.xlabel("Bucket Index")
    plt.ylabel("Number of Zeros")
    plt.title("Zeros of the Zeta Function in Alternating Buckets")
    plt.legend()
    plt.grid(True)
    plt.show()

# Function to visualize multiple spirals approach
def visualize_multiple_spirals(t_start, t_end, num_points=10000, spiral_count=10):
    ts, zeta_vals = zeta_values_on_critical_line(t_start, t_end, num_points)
    plt.figure(figsize=(10, 10))

    for i in range(spiral_count):
        spiral_ts = ts[i::spiral_count]
        spiral_vals = zeta_vals[i::spiral_count]
        re_vals = [mp.re(val) for val in spiral_vals]
        im_vals = [mp.im(val) for val in spiral_vals]
        plt.plot(re_vals, im_vals, label=f"Spiral {i+1}")

    plt.xlabel("Re(zeta(1/2 + it))")
    plt.ylabel("Im(zeta(1/2 + it))")
    plt.title("Multiple Spirals of Zeta Function on the Critical Line")
    plt.legend()
    plt.grid(True)
    plt.show()

# Set the interval and number of points for exploration
t_start = 0
t_end = 100
num_points = 10000

# Visualize alternating buckets
visualize_alternating_buckets(t_start, t_end, num_points)

# Visualize multiple spirals
visualize_multiple_spirals(t_start, t_end, num_points)
