"""
QUESTION:
Construct a function called `fibfib_with_offset` that takes two non-negative integers `n` and `offset` and returns the `n`-th element in a modified Fibonacci sequence, known as the FibFib sequence, where each term is the sum of the two preceding terms indexed by the previous two terms. The function should use dynamic programming to store pre-calculated values from `fibfib(offset)` to `fibfib(n+offset)`.
"""

def fibfib_with_offset(n: int, offset: int):
    fibfib_sequence = [0, 1] + [0] * (n + offset - 1)
    for i in range(2, n + offset + 1):
        fibfib_sequence[i] = fibfib_sequence[fibfib_sequence[i-1]] + fibfib_sequence[fibfib_sequence[i-2]]
    return fibfib_sequence[n + offset]