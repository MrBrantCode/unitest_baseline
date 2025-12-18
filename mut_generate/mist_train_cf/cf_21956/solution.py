"""
QUESTION:
Design a function `fibonacci(n)` that generates the first `n` numbers in the Fibonacci sequence using a single loop and no recursion. If `n` is less than or equal to 0, the function should return an empty list.
"""

def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        sequence = [0, 1]
        for i in range(2, n):
            sequence.append(sequence[i-1] + sequence[i-2])
        return sequence