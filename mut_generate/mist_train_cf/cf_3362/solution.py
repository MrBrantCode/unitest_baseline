"""
QUESTION:
Write a recursive function `sum_primes` that calculates the sum of all prime numbers in an array of numbers, ignoring negative numbers and zeros. The function should not use any loops or built-in sum functions and have a time complexity of O(n), where n is the length of the input array.
"""

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def sum_primes(array):
    if len(array) == 0:
        return 0
    else:
        if array[0] > 0 and is_prime(array[0]):
            return array[0] + sum_primes(array[1:])
        else:
            return sum_primes(array[1:])