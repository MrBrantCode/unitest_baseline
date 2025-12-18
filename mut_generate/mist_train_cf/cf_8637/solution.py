"""
QUESTION:
Write a function `remove_elements(nums)` that takes a list of positive integers as input and returns the modified list with all elements removed that have a prime index and are divisible by both 3 and 5.
"""

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def remove_elements(nums):
    modified_list = []
    for i, num in enumerate(nums):
        if not is_prime(i) or not (num % 3 == 0 and num % 5 == 0):
            modified_list.append(num)
    return modified_list