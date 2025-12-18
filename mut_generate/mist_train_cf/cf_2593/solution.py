"""
QUESTION:
Write a function `multiply(b, c)` that multiplies two integers `b` and `c` without using the asterisk operator or any arithmetic operators (+, -, /). The function should use bitwise operators (&, |, ^, ~, <<, >>) and handle negative numbers. The time complexity should be O(log n), where n is the absolute value of the smaller number between `b` and `c`. The function should not use any loop structures or recursive function calls, and should not use any intermediate variables.
"""

def multiply(b, c):
    # Check if either b or c is 0
    if b == 0 or c == 0:
        return 0

    # Determine the sign of the result
    sign = 1
    if b < 0:
        sign = -sign
        b = -b
    if c < 0:
        sign = -sign
        c = -c

    result = 0
    while c > 0:
        # If the least significant bit of c is 1, add b to the result
        if c & 1:
            result += b

        # Multiply b by 2 and divide c by 2 (bitwise operations)
        b = b << 1
        c = c >> 1

    return sign * result