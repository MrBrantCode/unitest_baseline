"""
QUESTION:
Write a function `prod_signs(arr)` that takes an array of integers as input. The function should return `None` if the array contains non-prime numbers, zero, or duplicate numbers (including both a prime integer and its negative counterpart). Otherwise, it should return the product of the signs of the unique integers (represented as -1 or 1) multiplied by the sum of the absolute values of the unique integers.
"""

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def entrance(arr):
    unique_values = set(arr)
    for val in unique_values:
        if not is_prime(abs(val)) or (val and -val in unique_values):
            return None

    prod = 1
    sum = 0
    for num in unique_values:
        prod *= num / abs(num)
        sum += abs(num)

    return prod * sum