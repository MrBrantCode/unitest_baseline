"""
QUESTION:
Write a function `find_largest_prime` that takes a list of integers as input and returns the largest prime number in the list. The function should have a time complexity of O(N), where N is the number of integers in the list, and a space complexity of O(1). The input list can contain integers ranging from 1 to 10^9, and the list size can be up to 10^7.
"""

import math

def is_prime(num):
    if num < 2:
        return False
    if num == 2 or num == 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    for i in range(5, int(math.sqrt(num)) + 1, 6):
        if num % i == 0 or num % (i + 2) == 0:
            return False
    return True

def find_largest_prime(numbers):
    largest_prime = 0
    for num in reversed(numbers):
        if is_prime(num):
            largest_prime = max(largest_prime, num)
    return largest_prime