"""
QUESTION:
Implement a function called `delete_primes` that takes in an array of integers and a number `n` as input, and returns the modified array with all prime numbers from the first `n` numbers deleted. The function should not use any built-in functions or libraries to check for prime numbers, and it should handle edge cases such as when `n` is less than or equal to 0, or when the array is empty.
"""

import math

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def delete_primes(arr, n):
    primes = []
    for i in range(min(n, len(arr))):
        if is_prime(arr[i]):
            primes.append(arr[i])
    modified_arr = []
    for num in arr:
        if num not in primes:
            modified_arr.append(num)
    return modified_arr