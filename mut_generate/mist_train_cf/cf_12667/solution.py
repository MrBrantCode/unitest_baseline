"""
QUESTION:
Create a function `calculate_exponent` that takes two numbers `x` and `y` as input and calculates the exponent of `x` raised to power `y`. The function should have a time complexity of O(log y) and a space complexity of O(1).
"""

def calculate_exponent(x, y):
    # base case
    if y == 0:
        return 1
    
    result = 1
    while y > 1:
        # if y is odd, multiply the result by x
        if y % 2 != 0:
            result *= x
        
        # reduce y by half and square x
        y = y // 2
        x = x * x
    
    return result * x