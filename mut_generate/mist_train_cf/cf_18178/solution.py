"""
QUESTION:
Write a recursive function named `sum_of_primes` to calculate the sum of all prime numbers in a given array. The function should not use any loops or built-in sum functions. The input array contains integers and the function should return the sum of prime numbers in the array.
"""

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def sum_of_primes(arr):
    if len(arr) == 0:
        return 0
    elif is_prime(arr[0]):
        return arr[0] + sum_of_primes(arr[1:])
    else:
        return sum_of_primes(arr[1:])