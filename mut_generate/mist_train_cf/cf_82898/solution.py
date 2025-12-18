"""
QUESTION:
Write a function `divide(dividend: int, divisor: int) -> int` that takes two integers as input and returns their quotient without using the division operator '/', any loops, and the math library. The function should handle division by zero by returning None.
"""

def divide(dividend: int, divisor: int) -> int:
    """
    Perform division of two integers without using the division operator '/',
    without using any loops, and without using the math library. If the 
    divisor is zero, then return None.
    """
    if divisor == 0:
        return None
    
    sign = 1 if (dividend < 0) == (divisor < 0) else -1
    dividend, divisor = abs(dividend), abs(divisor)
    
    quotient = 0
    temp = 0
    
    for i in range(31, -1, -1):
        if temp + (divisor << i) <= dividend:
            temp += divisor << i
            quotient |= 1 << i
    
    return sign * quotient