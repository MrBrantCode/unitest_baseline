"""
QUESTION:
Implement a function named `fibfib(n)` that calculates the nth element of the FibFib series. The FibFib series follows the rules: `fibfib(0) == 0`, `fibfib(1) == 0`, `fibfib(2) == 1`, and `fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3)`. The function should be efficient enough to compute the nth element for `n` up to 10,000.
"""

def fibfib(n):
    if n < 0:
        return "Please provide a positive integer"
    elif n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 1

    fibfib_list = [0, 0, 1] + [0] * (n - 2)

    for i in range(3, n + 1):
        fibfib_list[i] = fibfib_list[i - 1] + fibfib_list[i - 2] + fibfib_list[i - 3]

    return fibfib_list[n]