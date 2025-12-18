"""
QUESTION:
Create a function `triple_square_sum(lst)` that takes a list of integers as input and returns the cumulative sum of the cubes of even, non-negative integers that are not divisible by 5 and not prime numbers. If no valid numbers exist in the list, the function should return 0.
"""

def triple_square_sum(lst):
    def is_prime(n):
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

    def is_valid(n):
        return n >= 0 and n % 2 == 0 and not is_prime(n) and n % 5 != 0

    return sum(n**3 for n in lst if is_valid(n))