"""
QUESTION:
Write a function named `determine_sign` that determines the sign of a given decimal number without using any built-in functions or libraries. The function should be able to handle numbers up to 10^9 in magnitude and return "Zero" if the input is zero, "Positive" if the input is greater than zero, and "Negative" if the input is less than zero.
"""

def determine_sign(number):
    if number == 0:
        return "Zero"
    elif number > 0:
        return "Positive"
    else:
        return "Negative"