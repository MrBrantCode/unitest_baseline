"""
QUESTION:
Write a function named `sum_of_digits` that takes a positive integer `n` as input and returns the sum of its digits. Do not use built-in Python functions for converting the integer to a string or manipulating strings. The solution should have a time complexity of O(log n) and cannot use recursion or external libraries.
"""

def sum_of_digits(n):
    total = 0
    
    while n > 0:
        total += n % 10
        n //= 10
        
    return total