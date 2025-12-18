"""
QUESTION:
Create a function named `multiply` that takes two integers `x` and `y` as input and returns their product without using the multiplication operator (*) or any built-in multiplication functions. The function should have a time complexity of O(log n), where n is the value of the larger integer.
"""

def multiply(x, y):
    if x == 0 or y == 0:
        return 0
    
    result = 0
    while y > 0:
        if y & 1:
            carry = 0
            temp = result
            temp_x = x
            while temp_x > 0:
                carry = temp & temp_x
                temp = temp ^ temp_x
                temp_x = carry << 1
            result = temp
        x = x << 1
        y = y >> 1
    
    return result