"""
QUESTION:
Write a function named `find_index_of_prime_greater_than_23` that takes a sorted array of unique integers as input and returns the index of the first prime number greater than 23. The array must have at least 5 and no more than 20 elements. If no prime number greater than 23 exists in the array, return -1. The array must not be modified.
"""

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_index_of_prime_greater_than_23(arr):
    index = -1
    for i, num in enumerate(arr):
        if num > 23 and is_prime(num):
            index = i
            break
    return index