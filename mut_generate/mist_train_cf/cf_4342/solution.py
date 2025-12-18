"""
QUESTION:
Design a function `divide(dividend, divisor)` that takes two positive integers as input and returns their quotient without using the division operator. The function should have a time complexity of O(log N), where N is the number of digits in the dividend. If the divisor is zero, the function should return -1. The function should also handle the case where the signs of the dividend and divisor differ, returning a negative result if necessary.
"""

def divide(dividend, divisor):
    if divisor == 0:
        return -1
    
    is_negative = (dividend < 0) ^ (divisor < 0)
    dividend = abs(dividend)
    divisor = abs(divisor)
    quotient = 0
    
    while dividend >= divisor:
        power = 0
        while (divisor << power) <= dividend:
            power += 1
        power -= 1
        
        dividend -= divisor << power
        quotient += 1 << power
    
    if is_negative:
        quotient = -quotient
    
    return quotient