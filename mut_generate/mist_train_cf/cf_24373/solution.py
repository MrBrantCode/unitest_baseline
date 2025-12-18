"""
QUESTION:
Write a function `count_trailing_zeroes(factorial_number)` to calculate the number of trailing zeroes in the factorial of a given integer `factorial_number`. The input `factorial_number` is a positive integer, and the function should return a non-negative integer representing the count of trailing zeroes. The factorial of `factorial_number` is not provided, and the function should calculate the count without actually computing the factorial.
"""

def count_trailing_zeroes(factorial_number):
    # Initialize count 
    count = 0

    # Keep dividing n by powers of 5 and update count
    i = 5
    while (factorial_number/i>=1):
        count += int(factorial_number/i)
        i *= 5
        
    return int(count)