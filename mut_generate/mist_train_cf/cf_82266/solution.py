"""
QUESTION:
Create a function named `sum_primes` that takes an array of mixed data types as input and returns the sum of all prime numbers present in the array. The function should ignore non-integer values and use a custom function to check for prime numbers, without relying on any built-in or library functions.
"""

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for current in range(3, int(n ** 0.5) + 1, 2):
        if n % current == 0:
            return False
    return True

def sum_primes(arr):
    return sum(elem for elem in arr if type(elem) == int and is_prime(elem))