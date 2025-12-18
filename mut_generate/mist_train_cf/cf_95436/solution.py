"""
QUESTION:
Create a function `sum_even_to_n(n)` that calculates and returns the sum of even prime numbers from 2 to the given number `n`. The function should return the sum of only the prime even numbers in the given range.
"""

def sum_even_to_n(n):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    prime_sum = 0
    for num in range(2, n + 1, 2):
        if is_prime(num):
            prime_sum += num
    return prime_sum