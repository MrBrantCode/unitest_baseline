"""
QUESTION:
Complete the `is_multiply_prime` function which takes an integer 'a' as input, where 1 <= a <= 100. The function should return true if the given number is the product of 3 prime numbers, and false otherwise.
"""

def is_multiply_prime(a: int) -> bool:
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    prime_factors = []
    for i in range(2, a + 1):
        if a % i == 0 and is_prime(i):
            prime_factors.append(i)
    if len(prime_factors) == 3:
        product = 1
        for factor in prime_factors:
            product *= factor
        if product == a:
            return True
    return False