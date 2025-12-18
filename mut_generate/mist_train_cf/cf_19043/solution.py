"""
QUESTION:
Write a function `find_smallest_prime_index` that takes an array of integers as input and returns the index of the smallest prime number in the array. If there are multiple occurrences of the smallest prime number, return the index of the first occurrence. Assume that the input array is not empty and contains at least one prime number. The function should not modify the input array.
"""

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_smallest_prime_index(array):
    smallest_prime = float('inf')
    smallest_prime_index = -1
    for i, num in enumerate(array):
        if is_prime(num) and num < smallest_prime:
            smallest_prime = num
            smallest_prime_index = i
    return smallest_prime_index