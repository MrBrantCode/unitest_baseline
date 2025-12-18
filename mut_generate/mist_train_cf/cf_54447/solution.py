"""
QUESTION:
Write a function `fibfib_sequence(n: int, a: int, b: int, c: int)` that computes the n-th element of a modified FibFib sequence. The sequence is defined as follows: `fibfib(0) == a`, `fibfib(1) == b`, `fibfib(2) == c`, and `fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3)`. Use dynamic programming to efficiently compute the n-th element. The function should return the n-th element of the sequence.
"""

def fibfib_sequence(n: int, a: int, b: int, c: int) -> int:
    sequence = [a, b, c]
    if n < 3:
        return sequence[n]
    else:
        for i in range(3, n+1):
            sequence.append(sequence[i-1] + sequence[i-2] + sequence[i-3])
        return sequence[n]