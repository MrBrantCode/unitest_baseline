"""
QUESTION:
Write a function `second_smallest_prime` that takes an array of integers as input and prints the second smallest prime number in the array. The function should handle cases where there is no second smallest prime number. Assume the input array contains at least one integer.
"""

import math

def second_smallest_prime(arr):
    first_smallest = math.inf
    second_smallest = math.inf
    
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True
    
    for num in arr:
        if is_prime(num):
            if num < first_smallest:
                second_smallest = first_smallest
                first_smallest = num
            elif num < second_smallest and num != first_smallest:
                second_smallest = num
    
    if second_smallest != math.inf:
        return second_smallest
    else:
        return "There is no second smallest prime number in the array."