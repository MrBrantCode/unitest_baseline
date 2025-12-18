"""
QUESTION:
Implement a function `sum_of_primes(n)` that takes an integer `n` as input and returns the sum of all prime numbers up to `n`. The function should have a time complexity of O(n^(3/2)) and should not use any external libraries or built-in functions to check for prime numbers.
"""

def sum_of_primes(n):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    prime_sum = 0
    for num in range(2, n + 1):
        if is_prime(num):
            prime_sum += num
    return prime_sum