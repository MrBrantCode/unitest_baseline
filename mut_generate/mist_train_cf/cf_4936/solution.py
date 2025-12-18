"""
QUESTION:
Implement a function sum_primes(n) that calculates the sum of all prime numbers from 1 to a given positive integer n, excluding the number n itself. The function should return the sum of prime numbers and the count of prime numbers found. 

Restrictions: The function should have a time complexity of O(n * sqrt(m)) and a space complexity of O(1), where m is the current number being evaluated. The function should not use any external libraries or built-in functions that directly calculate prime numbers.
"""

def sum_primes(n):
    def is_prime(m):
        if m < 2:
            return False
        for i in range(2, int(m**0.5) + 1):
            if m % i == 0:
                return False
        return True

    prime_sum = 0
    prime_count = 0

    for i in range(2, n):
        if is_prime(i):
            prime_sum += i
            prime_count += 1

    return prime_sum, prime_count