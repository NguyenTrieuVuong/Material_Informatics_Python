import numpy as np
from scipy.integrate import quad
import math

f = lambda x: np.exp(np.cos(x))
N = 10**6
a = -math.pi
b = math.pi
F = 2.75

x = a + (b - a) * np.random.rand(N)
y = F * np.random.rand(N)
n = 0

for k in range(N):
    if (y[k] <= f(x[k])):
        n += 1  # Hit

I = F * (b - a) * n / N
Iref, _ = quad(f, a, b)

print("I =", I)
print("Iref =", Iref)
