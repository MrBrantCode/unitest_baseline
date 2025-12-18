"""
QUESTION:
Implement a function named `modified_function` that takes an integer as input and applies the following conditions:
- If the input is a positive integer, return the input multiplied by 2.
- If the input is a negative integer, return the absolute value of the input.
- If the input is 0, return 0.
"""

def modified_function(input_num):
    if input_num > 0:
        return input_num * 2
    elif input_num < 0:
        return abs(input_num)
    else:
        return 0