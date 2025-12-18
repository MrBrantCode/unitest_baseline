"""
QUESTION:
Create a function called `sort_string_by_delimiter` that takes a string of at least 3 comma-separated words as input, splits the string into an array using a comma as the delimiter, and returns the array in alphabetical order.
"""

def sort_string_by_delimiter(s):
    array = s.split(",")
    array.sort()
    return array