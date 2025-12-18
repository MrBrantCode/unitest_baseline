"""
QUESTION:
Design a function named `divide` that takes two positive integers `dividend` and `divisor` as input and returns their quotient without using the division operator. If `divisor` is zero, the function should return -1. The function should handle the case where the signs of `dividend` and `divisor` differ and return the correct negative result. The time complexity of the function should be O(log N), where N is the number of digits in `dividend`.
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