"""
QUESTION:
Write a function `count_digits` that takes an integer as input and returns the total number of digits in the integer, considering the negative sign as a digit if the number is negative. The input integer can be positive, negative, or zero.
"""

def count_digits(number):
    # Convert the number to a string and remove the negative sign if present
    number_str = str(abs(number))

    # Count the number of characters in the string (which gives the number of digits)
    num_digits = len(number_str)

    # Add 1 to the count if the number is negative
    if number < 0:
        num_digits += 1

    return num_digits