"""
QUESTION:
Write a function called `check_number` that takes one argument, which checks whether the input number is odd, even, or a decimal, and returns a corresponding string. The function should handle negative numbers and return an error message if the input is not a number.
"""

def check_number(num):
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