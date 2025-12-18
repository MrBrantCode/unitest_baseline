"""
QUESTION:
Implement a function `factorial_prime` that takes a list of integers as input and returns a new list. For each number in the input list, if the number is 0 or 1, the corresponding element in the output list should be -1. Otherwise, the corresponding element in the output list should be the factorial of the number. The function should be able to handle large numbers (greater than 50) efficiently.
"""

import math

def factorial_prime(input_list):
    '''Returns a list where each element is the factorial of the corresponding 
    element in the input list. If the number is 0 or 1, -1 is returned instead'''
    return [-1 if n in (0, 1) else math.factorial(n) for n in input_list]