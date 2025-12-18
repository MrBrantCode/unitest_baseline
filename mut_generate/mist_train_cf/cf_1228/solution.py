"""
QUESTION:
Construct a function "divisible_by" that takes a positive integer as input and returns a string indicating its divisibility by 3 and 5. The function should return one of four possible strings: 
- "The number is divisible by both 3 and 5" if the number is divisible by both.
- "The number is divisible by 3" if the number is divisible by 3 but not by 5.
- "The number is divisible by 5" if the number is divisible by 5 but not by 3.
- "The number is not divisible by 3 or 5" if the number is divisible by neither.

The function must not use any built-in mathematical functions to check for divisibility.
"""

def divisible_by(n):
    def is_divisible(dividend, divisor):
        while dividend >= divisor:
            dividend -= divisor
        return dividend == 0

    if is_divisible(n, 3) and is_divisible(n, 5):
        return "The number is divisible by both 3 and 5"
    elif is_divisible(n, 3):
        return "The number is divisible by 3"
    elif is_divisible(n, 5):
        return "The number is divisible by 5"
    else:
        return "The number is not divisible by 3 or 5"