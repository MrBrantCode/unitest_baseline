"""
QUESTION:
Implement a function `sum_and_product_of_primes(n)` that calculates the sum, product, and count of all prime numbers less than or equal to the given positive integer `n`, where `n` can be up to `10^9`. The function should have a time complexity less than `O(n^2)`, and it should not use any external libraries or modules for prime number generation or factorization. The function should return three values: the sum of prime numbers, the product of prime numbers, and the count of prime numbers.
"""

def sum_and_product_of_primes(n):
    prime_sum = 0
    prime_product = 1
    prime_count = 0

    def is_prime(i):
        if i <= 1:
            return False
        if i <= 3:
            return True
        if i % 2 == 0 or i % 3 == 0:
            return False
        for j in range(5, int(i ** 0.5) + 1, 6):
            if i % j == 0 or i % (j + 2) == 0:
                return False
        return True

    for i in range(2, n + 1):
        if is_prime(i):
            prime_sum += i
            prime_product *= i
            prime_count += 1
    return prime_sum, prime_product, prime_count