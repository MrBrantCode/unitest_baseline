"""
QUESTION:
Write a function `fibfib(n: int)` that calculates the nth element in the FibFib series, where `fibfib(n)` is the sum of the three preceding elements (`fibfib(n-1) + fibfib(n-2) + fibfib(n-3)`) with initial values `fibfib(0) = 0`, `fibfib(1) = 0`, and `fibfib(2) = 1`. Use dynamic programming to optimize the computation. The function should take an integer `n` as input and return the corresponding FibFib number.
"""

def fibfib(n: int):
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    
    fibfib_series = [0, 0, 1]
    
    for i in range(3, n+1):
        fibfib_series.append(fibfib_series[-1] + fibfib_series[-2] + fibfib_series[-3])
    
    return fibfib_series[-1]