import numpy as np
from scipy.integrate import nquad
import math

f = lambda x, y: x * np.cos(y) + y * np.sin(x) + 10
N = 10**6
a = math.pi
b = 2 * math.pi
c = 0
d = math.pi
Z = 16.5

x = a + (b - a) * np.random.rand(N)
y = c + (d - c) * np.random.rand(N)
z = Z * np.random.rand(N)
n = 0

for k in range(N):
    if (z[k] <= f(x[k], y[k])):
        n += 1  # Hit

I = Z * (b - a) * (d - c) * n / N
Iref, _ = nquad(f, [[a, b], [c, d]])

print("I =", I)
print("Iref =", Iref)
