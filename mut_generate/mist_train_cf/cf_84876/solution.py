"""
QUESTION:
Write a function `fibfib(n: int)` that calculates the nth element of a modified Fibonacci series, where fibfib(0) == 0, fibfib(1) == 0, fibfib(2) == 1, and fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3) for n > 2, using dynamic programming. The function should be able to handle values up to 10,000.
"""

def fibfib(n: int):
    fibfib_list = [0, 0, 1] + [0]*(n-2)
    for i in range(3, n+1):
        fibfib_list[i] = fibfib_list[i-1] + fibfib_list[i-2] + fibfib_list[i-3]
    return fibfib_list[n]