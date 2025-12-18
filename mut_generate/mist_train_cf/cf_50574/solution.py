"""
QUESTION:
Create a function `get_digits(text)` that takes a string `text` and returns a list of integers. The function should extract and convert all sequences of digits embedded in the string to integers, ignoring any non-digit characters. The input string can contain multiple sequences of digits separated by non-digit characters.
"""

def get_digits(text):
    import re
    return [int(i) for i in re.findall('\d+', text)]