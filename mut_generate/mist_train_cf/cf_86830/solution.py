"""
QUESTION:
Write a function named `fibonacci_sequence` that takes two parameters: `n`, the number of terms in the Fibonacci sequence, and `k`, the maximum product value. The function should calculate and return the Fibonacci sequence from 1 to `n` and the product of all the Fibonacci numbers. If the product exceeds `k`, the function should terminate the sequence generation and return the truncated sequence and product.
"""

def fibonacci_sequence(n, k):
    fib_sequence = []
    product = 1
    a, b = 0, 1

    while len(fib_sequence) < n:
        fib_sequence.append(b)
        product *= b

        if product > k:
            break

        a, b = b, a + b

    return fib_sequence, product