"""
QUESTION:
Create a function `is_odd_or_even(num)` that takes a single number as input and returns "Odd" if the number is odd, "Even" if the number is even, and "Error: Input is not a number" if the input is not a number. The function should handle negative numbers, decimals, and fractions. The check for odd or even must use bitwise operators.
"""

def is_odd_or_even(num):
    if isinstance(num, (int, float)):
        if isinstance(num, float) and num.is_integer():
            num = int(num)

        if num & 1:
            return "Odd"
        else:
            return "Even"
    else:
        return "Error: Input is not a number"