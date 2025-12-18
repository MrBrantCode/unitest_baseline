"""
QUESTION:
Create a function called `string_transform` that takes a list of strings as input and returns a generator that filters out strings with a length of 5 or less, converts the remaining strings to upper case, and yields them. The function should not store the transformed strings in memory, but instead produce them on-the-fly as they are needed.
"""

def string_transform(lst):
    return (s.upper() for s in lst if len(s) > 5)