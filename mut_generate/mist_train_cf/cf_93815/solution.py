"""
QUESTION:
Given a list of integers, find the sum of all the prime numbers in the list using Python.

Additional requirements:
- The solution should have a time complexity of O(n^2), where n is the length of the list.
- The solution should not use any built-in Python functions or libraries that directly calculate the sum of a list or check for prime numbers.
- The solution should be able to handle large lists efficiently.
- The solution should not use recursion.

Function name: sum_of_primes(lst) where lst is a list of integers.
"""

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def sum_of_primes(lst):
    prime_sum = 0
    for num in lst:
        if is_prime(num):
            prime_sum += num
    return prime_sum