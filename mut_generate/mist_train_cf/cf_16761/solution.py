"""
QUESTION:
Implement the "add_two_numbers" function to take two integers between -1000 and 1000 and return their sum. The function must use only bitwise operators and not utilize the "+" operator or any built-in functions for addition. The solution should be achieved in 10 lines of code or less.
"""

def add_two_numbers(a, b):
    while b != 0:
        carry = a & b
        a = a ^ b
        b = carry << 1
    return a