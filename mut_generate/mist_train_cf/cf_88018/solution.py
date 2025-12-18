"""
QUESTION:
Implement a function `sum_of_prime_elements` that takes an array of integers as input, computes the sum of all prime elements, and returns the result as a hexadecimal number. The input array can contain up to 1 million elements, each ranging from -1000 to 1000. The solution should have a time complexity of O(n) and a space complexity of O(1), where n is the size of the input array.
"""

import math

def sum_of_prime_elements(input_array):
    max_value = 1000  # Maximum possible value in the input array
    primes = [True] * (max_value + 1)
    primes[0] = primes[1] = False

    for i in range(2, int(math.sqrt(max_value)) + 1):
        if primes[i]:
            for j in range(i**2, max_value + 1, i):
                primes[j] = False

    sum_primes = 0
    for num in input_array:
        if 0 < num <= max_value and primes[num]:
            sum_primes += num

    return hex(sum_primes)