import numpy as np

f = lambda x: np.sqrt(1 - x**2)
N = 10**6
x = np.random.rand(N)
s = np.mean(f(x))
sopi = 4 * s
print(sopi)
