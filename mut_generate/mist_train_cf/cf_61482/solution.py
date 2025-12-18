"""
QUESTION:
Write a function named `fibfib` that takes an integer `n` and returns the nth element of a sequence where each element is the sum of the previous three elements, with initial values `fibfib(0) == 0`, `fibfib(1) == 0`, and `fibfib(2) == 1`. The function should be optimized to handle inputs up to 10,000.
"""

def fibfib(n: int):
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 1

    fibs = [0, 0, 1]

    for i in range(3, n + 1):
        fibs.append(fibs[i-1] + fibs[i-2] + fibs[i-3])

    return fibs[n]