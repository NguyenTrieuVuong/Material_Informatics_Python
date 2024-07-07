import numpy as np

N = 10**6
x = np.random.rand(N)
y = np.random.rand(N)
n = 0

for k in range(N):
    if (x[k]**2 + y[k]**2 <= 1):
        n += 1  # Hit

sopi = 4 * n / N
print(sopi)
