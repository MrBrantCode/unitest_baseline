"""
QUESTION:
Create a function called `check_hexadecimal` that takes a string representing a hexadecimal number as input and returns "Even" if the number is even and "Odd" if the number is odd. The function should not take any additional arguments other than the hexadecimal number.
"""

def check_hexadecimal(num):
    # Convert hexadecimal to decimal
    decimal_num = int(num, 16)

    # Check if the number is even or odd
    if decimal_num % 2 == 0:
        return "Even"
    else:
        return "Odd"