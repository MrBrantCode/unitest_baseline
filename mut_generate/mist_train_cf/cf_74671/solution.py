"""
QUESTION:
Create a function called `addTwoNumbers` that takes two non-negative integers `x` and `y` as input and returns their sum without using the standard arithmetic operators (+, -, *, /). The function should work using bitwise operations and handle the carry bits until there are no more carry bits left.
"""

def addTwoNumbers(x, y):
    # While loop runs until carry is 0 
    while (y != 0):
        
        # Carry now contains common set bits of x and y 
        carry = x & y 
  
        # Sum of bits of x and y where at least one of the bits is not set 
        x = x ^ y 
  
        # Carry is shifted by one so that adding it to x gives the required sum 
        y = carry << 1
    
    return x