"""
QUESTION:
Write a function `check_order(str)` that checks if the input string contains both numbers and alphabets in a specific order. The function should return `True` if the string contains both alphabets and numbers, and the alphabets come before the numbers. Otherwise, it should return `False`. The input string can contain a mix of upper and lower case alphabets and numbers. The length of the input string will not exceed 10^6.
"""

def check_order(s):
    has_alphabet = False
    has_number = False

    for char in s:
        if char.isalpha():
            has_alphabet = True
            if has_number:
                return False
        elif char.isnumeric():
            has_number = True
            if not has_alphabet:
                return False

    return has_alphabet and has_number