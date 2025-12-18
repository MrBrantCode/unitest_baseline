"""
QUESTION:
Implement a function `multiply_without_operator(a, b)` that multiplies two integers `a` and `b` without using the multiplication operator. The function should have a time complexity of O(log N), where N is the larger of the two numbers, and a space complexity of O(1). The function should handle both positive and negative integers as inputs and return the correct result.
"""

def multiply_without_operator(a, b):
    isNegative = False
    if (a < 0 and b >= 0) or (a >= 0 and b < 0):
        isNegative = True
    
    a = abs(a)
    b = abs(b)
    
    result = 0
    while a > 0:
        if a % 2 == 1:
            result += b
        a = a >> 1
        b = b << 1
    
    if isNegative:
        result = -result
    
    return result