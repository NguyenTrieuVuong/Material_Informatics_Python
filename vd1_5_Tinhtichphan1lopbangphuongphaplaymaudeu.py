import numpy as np
from scipy.integrate import quad
import math

f = lambda x: np.exp(np.cos(x))
N = 10**6
a = -math.pi
b = math.pi

x = a + (b - a) * np.random.rand(N)
Fm = np.mean(f(x))
I = Fm * (b - a)
Iref, _ = quad(f, a, b)

print("I =", I)
print("Iref =", Iref)
