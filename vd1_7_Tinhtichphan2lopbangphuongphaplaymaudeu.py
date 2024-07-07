import numpy as np
from scipy.integrate import nquad
import math

f = lambda x, y: x * np.cos(y) + y * np.sin(x) + 10
N = 10**6
a = math.pi
b = 2 * math.pi
c = 0
d = math.pi

x = a + (b - a) * np.random.rand(N)
y = c + (d - c) * np.random.rand(N)
Fm = np.mean(f(x, y))
I = Fm * (b - a) * (d - c)
Iref, _ = nquad(f, [[a, b], [c, d]])

print("I =", I)
print("Iref =", Iref)
