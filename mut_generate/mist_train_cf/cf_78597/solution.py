"""
QUESTION:
Design a function `multiply(x, y)` that calculates the product of two positive integers `x` and `y` without using the multiplication operator (`*`). The function should be optimized to minimize the number of additions and subtractions, with a time complexity better than O(y).
"""

def multiply(x, y):
    result = 0
    while(y > 0):
        # If second number becomes odd, add the first number to result 
        if((y & 1) == 1):
            result = result + x
 
        # Double the first number and halve the second number 
        x = x << 1
        y = y >> 1

    return result