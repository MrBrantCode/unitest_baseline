"""
QUESTION:
The function `sum_even_fibonacci(limit)` should calculate the sum of all even-valued Fibonacci numbers that do not exceed a given limit. Write a function that takes a single integer argument `limit`, generates Fibonacci numbers up to this limit, and returns the sum of the even-valued numbers in the sequence.
"""

def entrance(limit):
    a, b = 1, 2
    even_sum = 0

    # Keep going while our Fibonacci numbers are below the limit:
    while a < limit:
        # Every third fibonacci number is even, so add these:
        even_sum += a

        # Get the next three Fibonacci numbers:
        a, b = b, a + b
        b, a = a + b, b
        b, a = a + b, b

    return even_sum