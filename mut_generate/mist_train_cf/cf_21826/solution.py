"""
QUESTION:
Write a recursive function called `sum_multiples` that calculates the sum of all the multiples of 7 and 11 between 0 and a given positive integer `n` (inclusive), where `n` is less than or equal to 100. The function should not use any loops or conditional statements other than those allowed in the recursive function definition.
"""

def sum_multiples(n):
    if n < 7:  
        return 0
    elif n % 7 == 0 or n % 11 == 0:  
        return n + sum_multiples(n - 1)
    else:  
        return sum_multiples(n - 1)