"""
QUESTION:
Write a function named `fibonacci_series` that generates a Fibonacci series with n terms and checks if the series is a prime number. The function should take a single argument `n`, a positive integer greater than or equal to 2. It should return the generated Fibonacci series and whether it's a prime number or not.
"""

import math

def fibonacci_series(n):
    a = 0
    b = 1
    series = [a, b]

    for _ in range(3, n + 1):
        sum = a + b
        series.append(sum)
        a = b
        b = sum

    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                return False
        return True

    is_prime_series = all(is_prime(num) for num in series)

    return series, is_prime_series