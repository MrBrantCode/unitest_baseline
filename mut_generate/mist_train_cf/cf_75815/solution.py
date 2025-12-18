"""
QUESTION:
Create a function `sum_digits` that accepts an alphanumeric string as input and returns a tuple containing the sum of all individual digits, the largest digit found, and the smallest digit found. The function should be able to handle large alphanumeric strings and should return an error message for non-string inputs, empty strings, and strings without digits.
"""

def sum_digits(string):
    if not isinstance(string, str):
        return 'Invalid input. Function expects a string.'
    if not string:
        return 'Invalid input. String is empty.'

    digits = [int(ch) for ch in string if ch.isdigit()]

    if not digits:
        return 'No digits found in the string.'

    return sum(digits), max(digits), min(digits)