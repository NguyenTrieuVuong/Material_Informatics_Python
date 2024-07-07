def lcg(a, c, M, X0, n):
    """Generate n random numbers using the LCG method."""
    numbers = []
    X = X0
    for _ in range(n):
        X = (a * X + c) % M
        numbers.append(X)
    return numbers

# Test the generator with the values a = 111, c = 2, M = 256 and X1=1
a = 111
c = 2
M = 256
X1 = 1
n = 1000  # Generate 1000 numbers

numbers = lcg(a, c, M, X1, n)

# Determine the repetition period
repetition_period = len(set(numbers))
print("Repetition period:", repetition_period)
