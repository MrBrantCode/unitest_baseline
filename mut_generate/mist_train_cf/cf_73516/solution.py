"""
QUESTION:
Write a function named `sum_of_uniques` that takes a positive integer `limit` as input and returns the sum of all unique prime numbers below the given limit. A prime number is considered unique if it has no repeated digits. If the limit is less than 2, the function should return 0.
"""

def sum_of_uniques(limit):
    def is_prime(n):
        if n == 1 or n % 2 == 0:
            return n == 2
        d = 3
        while d * d <= n:
            if n % d == 0:
                return False
            d += 2
        return True

    def is_unique(n):
        return len(str(n)) == len(set(str(n)))

    return sum(i for i in range(2, limit) if is_prime(i) and is_unique(i))