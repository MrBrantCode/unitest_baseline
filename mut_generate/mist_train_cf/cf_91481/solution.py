"""
QUESTION:
Write a function named `multiply_without_operator` that multiplies two integers `b` and `c` without using the asterisk (*) operator or any arithmetic operators (+, -, /), only using bitwise operators (&, |, ^, ~, <<, >>). The function should run in O(log n) time complexity, where n is the value of the smaller number between `b` and `c`.
"""

def multiply_without_operator(b, c):
    result = 0
    
    while b > 0:
        if b & 1:  # check if b is odd
            result += c
        
        b >>= 1  # right shift b by 1 bit
        c <<= 1  # left shift c by 1 bit
    
    return result