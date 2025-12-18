"""
QUESTION:
Write a function `digit_product(a, b)` that takes two integers `a` and `b` and returns the product of their digits. The function should multiply each digit of `a` and each digit of `b` together to produce the result.
"""

def digit_product(a, b):
    product = 1
    
    # Convert integers to strings
    a_str = str(a)
    b_str = str(b)
    
    # Multiply each digit of a and b
    for digit in a_str:
        product *= int(digit)
    for digit in b_str:
        product *= int(digit)
    
    return product