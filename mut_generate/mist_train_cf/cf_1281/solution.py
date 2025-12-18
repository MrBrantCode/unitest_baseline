"""
QUESTION:
Create a function named `find_smallest_prime` that finds the smallest prime number in a given list of positive integers. The function should return -1 if no prime number is found in the list. The time complexity should be O(n√m), where n is the length of the list and m is the largest number in the list. The function should not use any external libraries or additional memory space apart from the input list and a few variables for iteration.
"""

import math

def find_smallest_prime(numbers):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    smallest_prime = -1
    for num in numbers:
        if is_prime(num):
            if smallest_prime == -1 or num < smallest_prime:
                smallest_prime = num
    return smallest_prime