"""
QUESTION:
Write a function `remove_digits(text)` that takes an alphanumeric string as input, removes all numerical digits from the string, and returns the resulting string. The function should be able to handle strings containing both letters and numbers.
"""

def remove_digits(text):
    result = ''.join([i for i in text if not i.isdigit()])
    return result