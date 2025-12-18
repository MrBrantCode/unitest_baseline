"""
QUESTION:
Write a function named `check_number(num)` that takes one argument `num` and returns a string indicating whether the number is odd, even, or a decimal. The function should also handle negative numbers and return an error message if the input is not a number.
"""

def entrance(num):
    if isinstance(num, (int, float)):
        if num % 1 == 0:
            if num % 2 == 0:
                return f"{num} is an even number."
            else:
                return f"{num} is an odd number."
        else:
            return f"{num} is a decimal number."
    else:
        return f"Error: {num} is not a number."