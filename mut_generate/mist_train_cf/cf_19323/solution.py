"""
QUESTION:
Write a function named `sum_of_primes(n)` that calculates the sum of all prime numbers less than or equal to the given positive integer `n`. The input `n` is within the range of 2 to 1000. The function should not use any built-in prime number functions or libraries and should have a time complexity of O(n^2).
"""

def sum_of_primes(n):
    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    prime_sum = 0
    for i in range(2, n+1):
        if is_prime(i):
            prime_sum += i
    return prime_sum