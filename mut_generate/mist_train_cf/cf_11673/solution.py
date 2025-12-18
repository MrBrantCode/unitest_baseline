"""
QUESTION:
Write a function called `extract_digits` that takes a string as input and returns a list of digits in the order they appear in the string. The input string may contain letters and digits, and may have leading or trailing whitespace. Do not use built-in functions or regular expressions, and aim for a time complexity of O(n), where n is the length of the input string.
"""

def extract_digits(s):
    digits = []
    current_digit = None

    for char in s:
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