import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, exp

# Initialize variables
N0 = 1e5
N = np.ones(int(N0))
T = 13
t = np.arange(1, 5*T+1)
p = np.log(2)/T
n = np.zeros(len(t))

# Main loop
for k in range(len(t)):
    r = np.random.rand(int(N0))
    N = N * (r > p)
    n[k] = np.sum(N)

# Plotting
plt.plot(t, n)

# Symbolic computation
t = symbols('t')
Nt = N0 * exp(-p*t)

# Plot symbolic function
t_values = np.linspace(0, 5*T, 400)
Nt_values = np.array([Nt.subs(t, ti).evalf() for ti in t_values])
plt.plot(t_values, Nt_values, 'r')

plt.show()
