"""
QUESTION:
Create a function called `find_prime_pairs` to find all pairs of prime numbers in a given array. The input array can contain both positive and negative numbers. The function should return a new array containing all pairs of prime numbers from the input array, without modifying the original array, and with a time complexity of O(n^2 * sqrt(k)), where n is the length of the input array and k is the maximum absolute value of the numbers in the array. The function should handle integers only and return the pairs in ascending order based on the first number in each pair.
"""

import math

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(abs(num))) + 1):
        if num % i == 0:
            return False
    return True

def find_prime_pairs(numbers):
    prime_pairs = []

    for i in range(len(numbers)):
        if not is_prime(numbers[i]):
            continue
        for j in range(i + 1, len(numbers)):
            if not is_prime(numbers[j]):
                continue
            prime_pairs.append((numbers[i], numbers[j]))

    return sorted(prime_pairs, key=lambda x: x[0])