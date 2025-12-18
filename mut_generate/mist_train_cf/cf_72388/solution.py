"""
QUESTION:
Develop a function `custom_fibonacci(n)` that generates a custom Fibonacci-like sequence. In this sequence, each corresponding term is multiplied by its position, and the new term is the sum of the last two terms after multiplication. The function should return a list of the first `n` terms of this sequence.
"""

def custom_fibonacci(n):
    a, b, sequence = 0, 1, []

    for i in range(1, n+1):
        sequence.append(a)
        a, b = b*i, a*i + b

    return sequence