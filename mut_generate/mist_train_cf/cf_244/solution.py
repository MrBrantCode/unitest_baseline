"""
QUESTION:
Create a function called `is_prime_with_three_factors` that takes an integer `num` as input. The function should return `True` if `num` is prime, has exactly three distinct prime factors, and the sum of these prime factors is greater than `num`. Otherwise, it should return `False`.
"""

def is_prime_with_three_factors(num):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    prime_factors = set()
    for i in range(2, num+1):
        if is_prime(i) and num % i == 0:
            prime_factors.add(i)

    return len(prime_factors) == 3 and sum(prime_factors) > num