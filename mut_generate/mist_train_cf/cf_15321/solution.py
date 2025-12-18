"""
QUESTION:
Write a function `calculate_e` to calculate the value of "e" to 4 decimal places without using any built-in math functions or libraries. The function should be able to handle large inputs and efficiently compute the value of "e" within a reasonable time frame.
"""

def calculate_e(n=100): 
    precision = 0.0001
    term = 1.0
    e = 2.0
    i = 2
    
    while abs(term) > precision and i < n:
        term *= 1.0 / i
        e += term
        i += 1
    
    return round(e, 4)