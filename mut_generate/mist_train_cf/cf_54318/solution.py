"""
QUESTION:
Create a function `clean_price_range` that takes a string representing a range of prices with currency as input. The function should remove the currency 'GBP', replace the dash '-' with a comma ',', remove any leading, trailing, or middle whitespaces, and convert the resulting string into a tuple of integers. The input string format is 'GBP X,XXX,XXX – GBP X,XXX,XXX' where 'X' is a digit.
"""

import re

def clean_price_range(s):
    cleaned = re.sub('GBP|\s|,', '', s)
    numbers = cleaned.split('–')
    return tuple(map(int, numbers))