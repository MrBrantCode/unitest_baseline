"""
QUESTION:
Write a function `divide_remainder(a, b)` that takes two positive integers `a` and `b` as input and returns the remainder of `a` divided by `b`. If `b` is zero, return "Cannot divide by zero". The function should have a time complexity of O(log(n)) and a space complexity of O(1), where n is the value of `a`, and should not use any built-in division or modulo operators.
"""

def divide_remainder(a, b):
    if b == 0:
        return "Cannot divide by zero"
    
    # Initialize the result 
    result = 0

    while a >= b:
        # Double the divisor 
        divisor = b
        power_of_2 = 1
        while (divisor << 1) <= a:
            divisor <<= 1
            power_of_2 <<= 1

        # Subtract the largest multiple of the divisor from the dividend
        a -= divisor
        result += power_of_2

    return a