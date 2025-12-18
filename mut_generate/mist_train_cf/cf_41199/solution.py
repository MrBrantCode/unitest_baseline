"""
QUESTION:
Write a function `check` that determines if a given number is prime, then use it to find the count of prime numbers within a given range. The function should take a single integer as input and return 1 if the number is prime, otherwise 0. The program should prompt the user to input the starting and ending numbers of the range, count the prime numbers within this range, and output the count and the time taken to find them. The program should handle the case where the starting number is greater than the ending number. The range should be inclusive, meaning it includes both the starting and ending numbers.
"""

import time
import math

def check(n):
    if n < 2:
        return 0
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return 0
    return 1