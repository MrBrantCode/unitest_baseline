"""
QUESTION:
Develop the `is_prime_and_largest_prime_factor(n)` function that checks if the input integer `n` is prime and calculates its largest prime factor. The function should return a tuple of form `(is_prime, largest_prime_factor)`, where `is_prime` indicates if the number is prime and `largest_prime_factor` is the largest prime factor of the number. If the number itself is prime, `is_prime` will be `True` and the `largest_prime_factor` will be the number itself.
"""

def is_prime_and_largest_prime_factor(n):
    def is_prime(num):
        """Check if num is a prime number"""
        if num == 1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def largest_prime_factor(num):
        """Find largest prime factor of num"""
        i = 2
        while i * i <= num:
            if num % i:
                i += 1
            else:
                num //= i
        return num

    return is_prime(n), largest_prime_factor(n)