"""
QUESTION:
Write a function named `calculate_e` that calculates the value of "e" to a specified number of decimal places without using any built-in math functions or libraries. The function should handle large inputs and compute the value efficiently. The result should be rounded to 4 decimal places.
"""

def calculate_e(n):
    term = 1.0
    e = 2.0
    
    for i in range(2, n):
        term *= 1.0 / i
        e += term
    
    return round(e, 4)