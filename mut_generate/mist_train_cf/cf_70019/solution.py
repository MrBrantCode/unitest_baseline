"""
QUESTION:
Develop a function named `fibonacci` that generates the first `n` numbers in the Fibonacci sequence, where each number is the sum of the two preceding ones, starting from 0 and 1, and `n` is a non-negative integer.
"""

def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        seq = [0, 1]
        while len(seq) < n:
            seq.append(seq[-1] + seq[-2])
        return seq