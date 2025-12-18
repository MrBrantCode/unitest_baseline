"""
QUESTION:
Write a function `multiply_abs_values_v2` that takes a list of numerical values as input and returns the multiplication result of the absolute values of these numbers, considering only their closest rounded-down integers. The function should also filter out elements that are divisible by any prime number less than or equal to 5 (i.e., 2, 3, or 5).
"""

def multiply_abs_values_v2(lst):
    import math

    def is_divisible_by_prime(n):
        primes = [2, 3, 5]
        for prime in primes:
            if n % prime == 0:
                return True
        return False

    result = 1
    for num in lst:
        int_num = math.floor(abs(num))
        if not is_divisible_by_prime(int_num):
            result *= int_num

    return result