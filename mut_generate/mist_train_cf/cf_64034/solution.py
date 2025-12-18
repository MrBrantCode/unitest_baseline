"""
QUESTION:
Write a function named `print_pattern(n)` that takes an integer `n` as input and prints a reversed numeric pattern from `n` to 1. The pattern should include the square root of each number, rounded to three decimal places, appended to the right of each row in descending order of square roots. Use recursion to print each row of the pattern, stopping when `n` becomes 0.
"""

import math

def print_pattern(n):
    if n < 1:
        return

    for i in range(n, 0, -1):
        print(i, end=' ')
        
    for i in range(n, 0, -1):
        print(round(math.sqrt(i), 3), end=' ')
    print()
    
    print_pattern(n-1)