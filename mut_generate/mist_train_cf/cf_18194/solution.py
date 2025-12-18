"""
QUESTION:
Create a function `split_string(string)` that takes a string as input, splits it into a list of strings using a comma as a delimiter, removes any leading or trailing spaces, ignores commas inside double quotation marks, and returns the list sorted in descending order based on the length of each string. The function should also handle cases with multiple consecutive spaces by replacing them with a single space.
"""

import csv

def split_string(s):
    # Replace consecutive spaces with a single space
    s = ' '.join(s.split())

    # Split the string using a comma as a delimiter, ignoring commas inside double quotes
    split_list = next(csv.reader([s], quotechar='"', delimiter=','))

    # Remove leading and trailing spaces from each element
    split_list = [element.strip() for element in split_list]

    # Sort the list in descending order based on the length of each string
    sorted_list = sorted(split_list, key=len, reverse=True)

    return sorted_list