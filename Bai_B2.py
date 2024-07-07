import numpy as np
import matplotlib.pyplot as plt

# Linear Congruential Generator (LCG)
def lcg(seed, a, c, m, n):
    numbers = [seed]
    for _ in range(n - 1):
        next_number = (a * numbers[-1] + c) % m
        numbers.append(next_number)
    return np.array(numbers) / m

# Box-Muller transformation
def box_muller_transform(u1, u2):
    z1 = np.sqrt(-2 * np.log(u1)) * np.cos(2 * np.pi * u2)
    z2 = np.sqrt(-2 * np.log(u1)) * np.sin(2 * np.pi * u2)
    return z1, z2

# LCG parameters
a = 22695477
c = 1
m = 2**32
n = 10**5

# Generate x1 and x2 using LCG
seed = 42  # Seed value
x1 = lcg(seed, a, c, m, n)
x2 = lcg(seed + 1, a, c, m, n)

# Box-Muller transformation
u1 = x1
u2 = x2
y1, y2 = box_muller_transform(u1, u2)

# Standardize the distributions
y1_standardized = (y1 - np.mean(y1)) / np.std(y1)
y2_standardized = (y2 - np.mean(y2)) / np.std(y2)

# Plot probability distributions
plt.figure(figsize=(12, 6))

plt.subplot(2, 2, 1)
plt.hist(x1, bins=50, density=True, label='x1 Distribution')
plt.title('x1 Distribution')
plt.xlabel('Value')
plt.ylabel('Probability Density')
plt.legend()

plt.subplot(2, 2, 2)
plt.hist(x2, bins=50, density=True, label='x2 Distribution')
plt.title('x2 Distribution')
plt.xlabel('Value')
plt.ylabel('Probability Density')
plt.legend()

plt.subplot(2, 2, 3)
plt.hist(y1_standardized, bins=50, density=True, label='y1 Distribution (Standardized)')
plt.title('y1 Distribution (Standardized)')
plt.xlabel('Value')
plt.ylabel('Probability Density')
plt.legend()

plt.subplot(2, 2, 4)
plt.hist(y2_standardized, bins=50, density=True, label='y2 Distribution (Standardized)')
plt.title('y2 Distribution (Standardized)')
plt.xlabel('Value')
plt.ylabel('Probability Density')
plt.legend()

plt.tight_layout()
plt.show()
