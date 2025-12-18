"""
QUESTION:
Create a function fibfib(x) that calculates the x-th component of the FibFib series, where fibfib(0) = 0, fibfib(1) = 0, fibfib(2) = 1, and fibfib(x) = fibfib(x-1) + fibfib(x-2) + fibfib(x-3) for x > 2. The function should efficiently determine the x-th component without redundant calculations.
"""

def fibfib(x):
    if x < 3:
        if x < 0:
            return -1
        else:
            return x == 2 and 1 or 0

    a, b, c = 0, 0, 1
    for _ in range(3, x+1):
        a, b, c = b, c, a + b + c
    return c