"""
QUESTION:
Create a function called `multiply` that takes two integers `a` and `b` as input and returns their product without using the multiplication operator or any built-in multiplication functions. The function should have a time complexity of O(log n), where n is the larger of the two input numbers, and should only use basic arithmetic operations such as addition, subtraction, and division.
"""

def multiply(a, b):
    # Check if either number is zero
    if a == 0 or b == 0:
        return 0
    
    # Check if either number is negative
    is_negative = (a < 0) ^ (b < 0)
    
    # Convert both numbers to positive
    a = abs(a)
    b = abs(b)
    
    # Swap numbers if necessary to make a the larger number
    if a < b:
        a, b = b, a
    
    # Initialize the result
    result = 0
    
    # Perform repeated addition of a to result
    while b > 0:
        # If b is odd, add a to result
        if b & 1:
            result += a
        
        # Double a and halve b
        a += a
        b >>= 1
    
    # If the result should be negative, negate it
    if is_negative:
        result = -result
    
    return result