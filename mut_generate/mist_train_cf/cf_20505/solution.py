"""
QUESTION:
Write a function `is_perfect_prime` to check if a given number is a perfect prime, which is a prime number equal to the sum of all its divisors. Additionally, implement a helper function `find_divisors` to find all divisors of a given number, excluding the use of external libraries or pre-defined functions.
"""

def find_divisors(n):
    """Finds all divisors of a given number."""
    divisors = []
    for i in range(1, n):
        if n % i == 0:
            divisors.append(i)
    return divisors


def is_perfect_prime(n):
    """Checks if a given number is a perfect prime."""
    def is_prime(num):
        """Checks if a number is prime."""
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    divisors = find_divisors(n)
    return is_prime(n) and n == sum(divisors)