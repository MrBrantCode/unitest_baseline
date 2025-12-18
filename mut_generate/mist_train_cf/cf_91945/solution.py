"""
QUESTION:
Write a function called `extract_digits` that takes a string as input and returns a list of digits found in the string. The digits in the list should be in the same order as they appear in the string. The function should not use any built-in functions or regular expressions. The input string may contain letters and whitespace, and may have leading or trailing whitespace. The function should have a time complexity of O(n), where n is the length of the input string.
"""

def extract_digits(string):
    digits = []
    current_digit = None

    for char in string:
        if char.isdigit():
            if current_digit is None:
                current_digit = int(char)
            else:
                current_digit = current_digit * 10 + int(char)
        elif current_digit is not None:
            digits.append(current_digit)
            current_digit = None

    if current_digit is not None:
        digits.append(current_digit)

    return digits