"""
QUESTION:
Check if a given string contains both alphabets and numbers in a specific order. The function `check_order(str)` should return True if the string contains at least one alphabet followed by at least one number, and False otherwise. The input string can be a mix of upper and lower case alphabets and numbers, and its length will not exceed 10^6.
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