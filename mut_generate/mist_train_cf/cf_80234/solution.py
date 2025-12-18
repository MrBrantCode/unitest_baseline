"""
QUESTION:
Write a function `replace_prime_with_cubic_exp(arr)` that takes an array of integers as input, replaces each prime number with its cubic exponent, and returns the modified array. A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself. The cubic exponent of a number is the number raised to the power of 3.
"""

def replace_prime_with_cubic_exp(arr):
    def is_prime(num):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    return False
            else:
                return True
        else:
            return False

    return [num**3 if is_prime(num) else num for num in arr]