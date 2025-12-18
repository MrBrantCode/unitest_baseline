"""
QUESTION:
Given variables x and y, where x is initially set to 7 and y is set to the value of x, calculate the final value of x after the following operations are performed sequentially: 
1. x is set to the sum of its current value, y, and 2. 
2. y is set to the sum of its current value, x, and then subtract 1.
3. x is set to the product of y and x, divided by 2.
"""

def calculate_x(x, y):
    x = x + y + 2
    y = y + x - 1
    x = (y * x) // 2
    return x