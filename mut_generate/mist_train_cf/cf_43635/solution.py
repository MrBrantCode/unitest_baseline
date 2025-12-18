"""
QUESTION:
Design a function `sum_of_even_fib(n)` that calculates the sum of even Fibonacci numbers less than or equal to a given number `n`. The function should be optimized for larger inputs.
"""

def sum_of_even_fib(n):
    if n < 2:
        return 0
    # Initialize first two even prime numbers
    # and their sum
    fib_1 = 0    # fib(0)
    fib_2 = 2    # fib(3)
    sum_even = fib_1 + fib_2

    # Calculate sum of remaining terms
    while fib_2 <= n:
        # next Fibonacci number is even if it is 4 times of previous 
        # even number plus the prior even number, fib(i) = 4*fib(i-3) + fib(i-6)
        fib_3 = 4 * fib_2 + fib_1

        # If we've gone past sum, we break loop
        if fib_3 > n:
            break

        # Move to the next even number and update sum
        fib_1, fib_2 = fib_2, fib_3
        sum_even += fib_2
    return sum_even