"""
QUESTION:
Count the number of prime numbers in a list that contain the digit 3. 

The input is a list of integers, and the output should be the count of prime numbers containing the digit 3. 

The solution must have a time complexity of O(n log(log n)), where n is the number of elements in the list. 

Assume the input list only contains positive integers.
"""

import math

def is_prime_and_contains_3(num):
    if num < 2:
        return False
    if '3' not in str(num):
        return False

    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False

    return True