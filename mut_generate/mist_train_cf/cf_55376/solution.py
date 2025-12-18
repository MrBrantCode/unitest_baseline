"""
QUESTION:
Write a function `sum_of_multiples(n)` that calculates the sum of all multiples of 3 and 5 below a given number `n`. The function should take one integer argument `n` and return the sum as an integer.
"""

def sum_of_multiples(n):
    total = 0
    for i in range(n): 
        if i % 3 == 0 or i % 5 == 0: 
            total += i 
    return total