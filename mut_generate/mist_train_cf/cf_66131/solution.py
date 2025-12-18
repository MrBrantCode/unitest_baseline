"""
QUESTION:
Construct a boolean function named "is_num_even" that accepts an integer input and returns true if the provided integer is an even number. The function should not use any arithmetic, bitwise, or comparison operators. The input should be handled as a string to check the last digit, and the function should return false for any invalid input.
"""

def is_num_even(n):
    try:
        str_n = str(n)
        last_digit = str_n[-1]
        return last_digit in '02468'
    except Exception as e:
        return False