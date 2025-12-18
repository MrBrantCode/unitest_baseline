"""
QUESTION:
Write a function named `fibonacci_sequence` that takes two parameters, `n` and `k`, where `n` is a positive integer representing the number of Fibonacci numbers to generate and `k` is a positive integer representing the maximum allowed product of Fibonacci numbers. The function should return a list of the first `n` Fibonacci numbers and their product, but terminate and return the list and product as soon as the product exceeds `k`. The function should be able to handle large values of `n` and `k` efficiently.
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