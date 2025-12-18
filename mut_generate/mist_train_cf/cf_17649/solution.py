"""
QUESTION:
Write a function called `format_number` that takes a float as input, rounds it to the nearest hundredth, and returns a string with two decimal points, a comma as the thousand separator, and a period as the decimal separator.
"""

def format_number(num):
    return "{:,.2f}".format(round(num, 2))