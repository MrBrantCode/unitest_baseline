"""
QUESTION:
Create a function `fibonacci_reverse(n)` that generates a Fibonacci sequence of length `n`, where the first two numbers are 0 and 1, and each subsequent number is the sum of the previous two. Return the sequence in reverse order.
"""

def fibonacci_reverse(n):
    sequence = [0, 1]
    for i in range(2, n):
        sequence.append(sequence[i-1] + sequence[i-2])
    sequence.reverse()
    return sequence