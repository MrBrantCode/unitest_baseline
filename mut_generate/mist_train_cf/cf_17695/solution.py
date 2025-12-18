"""
QUESTION:
Write a function called `determine_sign()` that takes a number as input and returns its sign as a string. The function should return "Negative" if the number is less than zero, "Positive" if the number is greater than zero, and "Zero" if the number is equal to zero. The function should not use any built-in functions or libraries for determining the sign of a number and should be able to handle decimal numbers up to 10^18 in magnitude.
"""

def determine_sign(number):
    if number < 0:
        return "Negative"
    elif number > 0:
        return "Positive"
    else:
        return "Zero"