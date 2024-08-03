import numpy as np
from mpmath import mp, zeta, mpc

# Set high precision
mp.dps = 50

# Function to calculate zeta function values on the critical line
def zeta_values_on_critical_line(t_start, t_end, num_points=1000):
    ts = np.linspace(t_start, t_end, num_points)
    zeta_vals = [zeta(mpc(0.5, t)) for t in ts]
    return ts, zeta_vals

# Function to calculate and visualize alternating buckets
def alternating_buckets_detection(t_start, t_end, num_points=1000, max_bucket_size=1000):
    ts, zeta_vals = zeta_values_on_critical_line(t_start, t_end, num_points)
    found_zero = False

    for bucket_size in range(1, max_bucket_size + 1):
        for i in range(0, len(ts), bucket_size):
            bucket = zeta_vals[i:i+bucket_size]
            zeros_count = sum(abs(mp.re(z)) < 1e-12 and abs(mp.im(z)) < 1e-12 for z in bucket)
            if zeros_count > 0:
                print(f"Bucket size {bucket_size}, Bucket {i//bucket_size + 1}: {zeros_count} zeros")
                found_zero = True

    if not found_zero:
        print("No zeros detected in any bucket")

# Set the interval and number of points for exploration
t_start = 0
t_end = 100
num_points = 1000
max_bucket_size = num_points

# Detect zeros in alternating buckets
alternating_buckets_detection(t_start, t_end, num_points, max_bucket_size)
