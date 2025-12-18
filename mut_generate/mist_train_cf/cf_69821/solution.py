"""
QUESTION:
Write a function named `prime_cubes_fib_diff(n)` that takes an integer `n` as input, calculates the sum of cubes of the first `n` prime numbers and the sum of the first `n` Fibonacci numbers, and returns their difference. The function should handle cases where `n` is not a natural number by returning an error message. The function should be optimized to efficiently handle large inputs.
"""

def prime_cubes_fib_diff(n):
    if not isinstance(n, int) or n < 1:
        return "Invalid input. Please enter a natural number."

    prime_sum, fib_sum = 0, 0
    prime_count, number = 0, 2
    while prime_count < n:
        if is_prime(number):
            prime_sum += number ** 3
            prime_count += 1
        number += 1

    a, b = 0, 1
    for _ in range(n):
        fib_sum += a
        a, b = b, a + b

    return prime_sum - fib_sum

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True

    if n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6

    return True