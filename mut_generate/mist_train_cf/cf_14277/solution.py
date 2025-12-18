"""
QUESTION:
Write a function to find all prime numbers within a specified range. The function should take two integers, lower_limit and upper_limit, as input and return a list of all prime numbers between lower_limit and upper_limit (inclusive). The input integers are assumed to be non-negative and lower_limit is less than or equal to upper_limit.
"""

def find_primes_in_range(lower_limit, upper_limit):
    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    primes = [num for num in range(lower_limit, upper_limit + 1) if is_prime(num)]
    return primes