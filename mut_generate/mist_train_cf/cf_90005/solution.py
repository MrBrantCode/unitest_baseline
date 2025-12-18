"""
QUESTION:
Write a function named `is_prime_with_factors` that takes a positive integer greater than 1 as input and returns a tuple containing a boolean value indicating whether the number is prime and a list of tuples representing the prime factors of the number along with their multiplicities.
"""

def is_prime_with_factors(number):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def prime_factors(n):
        factors = []
        i = 2
        while i <= n:
            if n % i == 0:
                count = 0
                while n % i == 0:
                    n //= i
                    count += 1
                factors.append((i, count))
            i += 1
        return factors

    prime = is_prime(number)
    factors = prime_factors(number)

    return prime, factors