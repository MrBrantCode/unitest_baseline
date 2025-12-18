"""
QUESTION:
Design a function `complex_arithmetic` that takes two complex numbers `c1` and `c2` as input. The function should perform complex arithmetic operations (addition, subtraction, multiplication, and division) on the input numbers, handle exceptions for division by zero, and return the results of these operations along with the conjugate product of the two complex numbers. The function should return a tuple containing the results of the addition, subtraction, multiplication, division, and conjugate product operations.
"""

def complex_arithmetic(c1, c2):
    try:
        add = c1 + c2
        diff = c1 - c2
        prod = c1 * c2
        div = c1 / c2 if c2 != 0 else "Cannot divide by zero"
    except ZeroDivisionError:
        div = "Cannot divide by zero"
        
    conjugate_product = c1.conjugate() * c2.conjugate()
    
    return add, diff, prod, div, conjugate_product