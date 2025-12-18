"""
QUESTION:
Implement a function `multiply(x, y)` that takes two integers as input and returns their product. The function must handle cases where one or both of the input numbers are negative. The implementation should only use bitwise operations, bitwise shifting, and basic arithmetic operations, without utilizing the multiplication operator (*) or any built-in multiplication functions.
"""

def multiply(x, y):
    # Check if either number is negative
    is_negative = False
    if x < 0:
        x = -x
        is_negative = not is_negative
    if y < 0:
        y = -y
        is_negative = not is_negative
    
    # Initialize the product
    product = 0
    
    # Perform bitwise addition to calculate the product
    while y > 0:
        # If y is odd, add x to the product
        if y & 1:
            product += x
        
        # Double x and divide y by 2 (right shift)
        x <<= 1
        y >>= 1
    
    # If the result is negative, negate it
    if is_negative:
        product = -product
    
    return product