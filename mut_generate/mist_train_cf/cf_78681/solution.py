"""
QUESTION:
Write a function named `remove_primes` that takes an array of numbers as input, removes all prime numbers from the array, and returns the resulting array. The function should handle special cases where the numbers are either negative or zero. The input array should be a list of numbers, and the function should not use any built-in functions to populate the list. The numbers in the array can be integers or floating-point numbers.
"""

def is_prime(n):
    """ Check if the number is prime """
    if int(n) != n or n < 2:  # revised to handle non-integer inputs
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def remove_primes(arr):
    """ Remove all the prime numbers from the array """
    new_arr = []
    for n in arr:
        if not is_prime(n):
            new_arr.append(n)
    return new_arr