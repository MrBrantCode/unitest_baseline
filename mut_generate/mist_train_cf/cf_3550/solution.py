"""
QUESTION:
Write a function sum_of_prime_elements that takes an array of integers as input, where the array can contain up to 1 million elements, each ranging from -1000 to 1000. The function should compute the sum of all prime elements in the array and return the result as a hexadecimal number. The solution should have a time complexity of O(n) and a space complexity of O(1).
"""

import math

def sum_of_prime_elements(arr):
    max_value = 1000
    primes = [True] * (max_value + 1)
    primes[0] = primes[1] = False

    for i in range(2, int(math.sqrt(max_value)) + 1):
        if primes[i]:
            for j in range(i**2, max_value + 1, i):
                primes[j] = False

    sum_primes = 0
    for num in arr:
        if num > 0 and primes[num]:
            sum_primes += num

    return hex(sum_primes)