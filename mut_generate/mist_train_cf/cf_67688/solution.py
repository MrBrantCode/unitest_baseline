"""
QUESTION:
Write a function called `is_prime` to check if a number is prime or not, and use it in a generator expression to generate prime numbers from a list of integers. The `is_prime` function should return `True` if the number is prime, `False` otherwise. The generator expression should yield the prime numbers in the order they appear in the list. The input list contains only integers. The solution should be memory-efficient and capable of handling large lists.
"""

def is_prime(n):
    if n < 2:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    else:
        for current in range(3, int(n ** 0.5) + 1, 2):
            if n % current == 0:
                return False
        return True