import mpmath
from mpmath import zetazero
import numpy as np

# Set high precision
mpmath.mp.dps = 50  # Decimal places

# Generate a list of Riemann zeta function zeros
def generate_riemann_zeros(n):
    zeros = [float(zetazero(i).imag) for i in range(1, n+1)]
    return zeros

# Number of zeros to generate
num_zeros = 10000

# Generate the zeros
zeros = generate_riemann_zeros(num_zeros)

# Format the zeros as a numpy array
formatted_zeros = np.array(zeros)

# Print the formatted zeros
print("known_zeros = np.array([", end="")
for i, zero in enumerate(formatted_zeros):
    if i == len(formatted_zeros) - 1:
        print(f"{zero}])")
    else:
        print(f"{zero}, ", end="")
