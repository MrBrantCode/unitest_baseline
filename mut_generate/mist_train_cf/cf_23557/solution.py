"""
QUESTION:
Create a function `is_even` that takes an integer `num` as input and returns a boolean value indicating whether the number is even or not. The solution should only use the logical operators 'or', 'and', and 'not' in combination with the modulus operator.
"""

def is_even(num):
    return (num % 2 == 0) or ((not num % 2 == 0) and (not num % 2 == 1))