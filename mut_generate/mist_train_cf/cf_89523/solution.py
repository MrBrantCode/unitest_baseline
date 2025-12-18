"""
QUESTION:
Design a function named `largest_prime` that takes an array of integers as input and returns the largest prime number in the array. The function should have a time complexity of O(n), where n is the length of the array, and it should not use any built-in sorting or max functions.
"""

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def largest_prime(arr):
    largest = None
    for num in arr:
        if is_prime(num):
            if largest is None or num > largest:
                largest = num
    return largest