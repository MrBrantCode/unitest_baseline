"""
QUESTION:
Create a function called `multiply` that takes two integers as input and returns their product without using the multiplication operator (*). The function should handle both positive and negative integers and return a result with the correct sign.
"""

def multiply(num_1, num_2):
    if num_1 == 0 or num_2 == 0:
        return 0
    
    sign = 1
    if num_1 < 0:
        num_1 = -num_1
        sign = -sign
    if num_2 < 0:
        num_2 = -num_2
        sign = -sign
    
    result = 0
    for _ in range(num_2):
        result += num_1
    
    return sign * result