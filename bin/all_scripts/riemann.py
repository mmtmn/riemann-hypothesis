import mpmath
from mpmath import mp, zeta, mpc
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Set high precision
mp.dps = 50  # Decimal places

# Function to find zeros on the critical line with high precision
def find_zeros_on_critical_line(t_start, t_end, num_points=10000):
    ts = np.linspace(t_start, t_end, num_points)
    zeros = []
    for t in ts:
        z = zeta(mpc(0.5, t))
        if abs(z) < 1e-10:
            zeros.append(t)
    return zeros

# Define the interval for exploration
t_start = 0
t_end = 100
num_points = 10000

# Find and print zeros on the critical line in the interval
zeros = find_zeros_on_critical_line(t_start, t_end, num_points)
print(f"Zeros on the critical line between {t_start} and {t_end}: {zeros}")

# Visualize the zeros
plt.scatter([0.5]*len(zeros), zeros, color='red')
plt.xlabel("Re(s)")
plt.ylabel("Im(s)")
plt.title("Zeros of the Zeta Function on the Critical Line")
plt.grid(True)
plt.show()

# Known zeros of the zeta function (example data)
known_zeros = np.array([14.134725, 21.022040, 25.010858, 30.424876, 32.935062, 37.586178, 40.918719, 43.327073])

# Generate features and labels for training
X = np.arange(len(known_zeros)).reshape(-1, 1)
y = known_zeros

# Train a linear regression model
model = LinearRegression()
model.fit(X, y)

# Predict the next zero
next_zero_index = len(known_zeros)
next_zero_prediction = model.predict([[next_zero_index]])
print(f"Predicted next zero: {next_zero_prediction[0]}")

# Visualize the known zeros and the prediction
plt.scatter(X, y, color='blue', label='Known Zeros')
plt.scatter([next_zero_index], next_zero_prediction, color='red', label='Predicted Zero')
plt.xlabel("Index")
plt.ylabel("Im(s)")
plt.title("Prediction of Next Zero of the Zeta Function")
plt.legend()
plt.grid(True)
plt.show()

# Function to visualize the zeta function values on the critical line
def visualize_critical_line(t_start, t_end, num_points=10000):
    ts = np.linspace(t_start, t_end, num_points)
    zeta_values = [zeta(mpc(0.5, t)) for t in ts]
    re_vals = [mpmath.re(val) for val in zeta_values]
    im_vals = [mpmath.im(val) for val in zeta_values]

    plt.figure(figsize=(14, 7))
    plt.plot(ts, re_vals, label="Re(zeta(1/2 + it))")
    plt.plot(ts, im_vals, label="Im(zeta(1/2 + it))")
    plt.xlabel("t")
    plt.ylabel("Zeta Function Values")
    plt.title("Zeta Function on the Critical Line")
    plt.legend()
    plt.grid(True)
    plt.show()

# Visualize the zeta function on the critical line
visualize_critical_line(t_start, t_end, num_points)
