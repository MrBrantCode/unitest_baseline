"""
QUESTION:
Write a function called `find_divisors_and_prime_status` that takes a positive integer `n` as input. The function should return a list of tuples, where each tuple contains a divisor of `n` and a boolean indicating whether the divisor is prime or not. The divisors should be listed in ascending order.

Restriction: The input `n` will be a positive integer. The function should only consider divisors in the range from 1 to `n` (inclusive).
"""

def find_divisors_and_prime_status(n):
    def is_prime(number):
        if number <= 1:
            return False
        if number <= 3:
            return True
        if number % 2 == 0 or number % 3 == 0:
            return False
        i = 5
        while i * i <= number:
            if number % i == 0 or number % (i + 2) == 0:
                return False
            i += 6
        return True

    divisors = [(i, is_prime(i)) for i in range(1, n + 1) if n % i == 0]
    return divisors