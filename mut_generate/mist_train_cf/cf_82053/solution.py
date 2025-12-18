"""
QUESTION:
Write a function named `multiply` that takes two integers `b` and `c` as input and returns their product without using the asterisk (`*`) operator or built-in multiplication functions. The function should handle edge cases where `b` and/or `c` can be negative integers or zero.
"""

def multiply(b, c):
    # b == 0 or c == 0, returns 0
    if b == 0 or c == 0:
        return 0
    
    # If negative number exists, change the flag
    result, flag = 0, 1
    if (b < 0) ^ (c < 0):  # XOR operation, if there's only one negative number
        flag = -1

    b, c = abs(b), abs(c)  # convert both numbers to positive
    for _ in range(c):
        result += b
    return result * flag  # multiply with flag so as to return correct sign in result