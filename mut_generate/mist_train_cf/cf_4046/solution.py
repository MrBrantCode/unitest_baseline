"""
QUESTION:
Write an efficient function `divide_remainder(a, b)` that takes two positive integers `a` and `b` as input, returns the remainder of `a` divided by `b`, and handles the case when `b` is zero by returning the error message "Cannot divide by zero". The function should have a time complexity of O(log(n)), where n is the value of `a`, and a space complexity of O(1). The function should not use any built-in division or modulo operators.
"""

def divide_remainder(a, b):
    if b == 0:
        return "Cannot divide by zero"
    
    result = 0
    power = 1

    while a >= b:
        divisor = b
        power_of_2 = 1
        while (divisor << 1) <= a:
            divisor <<= 1
            power_of_2 <<= 1

        a -= divisor
        result += power_of_2

    return a