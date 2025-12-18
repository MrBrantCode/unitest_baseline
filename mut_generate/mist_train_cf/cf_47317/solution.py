"""
QUESTION:
Construct a function named `compare_strings` that takes two strings as input and returns `True` if they contain the same set of characters with the same frequency, regardless of their original order, and `False` otherwise. The comparison should be case-insensitive.
"""

def compare_strings(string1, string2):
    # Convert the strings to lower case and sort their characters
    string1 = sorted(string1.lower())
    string2 = sorted(string2.lower())

    # Compare if both the sorted strings are equal
    return string1 == string2