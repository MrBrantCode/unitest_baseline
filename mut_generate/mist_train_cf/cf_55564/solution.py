"""
QUESTION:
Write a function `fibfib_with_offset(n: int, offset: int)` that uses dynamic programming to calculate the `n`-th element in the FibFib sequence with a non-negative offset. The function should store pre-calculated values within the range of `fibfib(offset)` to `fibfib(n+offset)` for efficiency.
"""

def fibfib_with_offset(n: int, offset: int):
    fibfib = [1] * (n + offset + 1)

    for i in range(max(offset, 2), n + offset + 1):
        fibfib[i] = fibfib[fibfib[i-1]] + fibfib[fibfib[i-2]]

    return fibfib[n + offset]