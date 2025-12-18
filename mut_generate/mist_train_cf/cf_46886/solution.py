"""
QUESTION:
Write a function named `multiply` that takes a non-empty list of integers as input. The function should multiply all odd numbers in the list that are at even indices, divisible by 3, and immediately followed by a prime number in the list. The function should return the product of these numbers.
"""

def multiply(lst):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    result = 1
    for i in range(0, len(lst), 2):
        if lst[i] % 2 == 1 and lst[i] % 3 == 0 and i + 1 < len(lst) and is_prime(lst[i + 1]):
            result *= lst[i]
    return result