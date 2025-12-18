"""
QUESTION:
Implement a function `find_largest_prime` that takes a list of integers as input and returns the largest prime number in the list. The function should have a time complexity of O(N) and a space complexity of O(1), where N is the number of integers in the list. The integers in the list can range from 1 to 10^9.
"""

import math

def find_largest_prime(numbers):
    largest_prime = 0
    for num in sorted(numbers, reverse=True):
        if num < 2:
            continue
        if num == 2 or num == 3:
            return num
        if num % 2 == 0 or num % 3 == 0:
            continue
        for i in range(5, int(math.sqrt(num)) + 1, 6):
            if num % i == 0 or num % (i + 2) == 0:
                break
        else:
            return num
    return largest_prime