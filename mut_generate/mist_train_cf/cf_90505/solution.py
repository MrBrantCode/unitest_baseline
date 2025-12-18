"""
QUESTION:
Create a function named `find_prime_pairs` that takes an array of numbers as input and returns a new array containing all pairs of prime numbers from the input array, in ascending order based on the first number in each pair. The function should not modify the original array and have a time complexity of O(n^2 * sqrt(k)), where n is the length of the input array and k is the maximum absolute value of the numbers in the array.
"""

import math

def find_prime_pairs(numbers):
    prime_pairs = []

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(math.sqrt(abs(num))) + 1):
            if num % i == 0:
                return False
        return True

    for i in range(len(numbers)):
        if not is_prime(numbers[i]):
            continue
        for j in range(i + 1, len(numbers)):
            if not is_prime(numbers[j]):
                continue
            prime_pairs.append((numbers[i], numbers[j]))

    return sorted(prime_pairs, key=lambda x: x[0])