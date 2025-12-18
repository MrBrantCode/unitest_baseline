"""
QUESTION:
Write a function called `extract_digits(s)` that takes a string `s` as input and returns a list of digits found in the string. The function should not use any built-in functions or regular expressions. The string contains only digits and letters, with no whitespace. The function should have a time complexity of O(n), where n is the length of the input string. The output list should contain the digits in the same order as they appear in the string.
"""

def extract_digits(s):
    digits = []
    current_digit = ""
    
    for char in s:
        if char.isdigit():
            current_digit += char
        elif current_digit:
            digits.append(int(current_digit))
            current_digit = ""
    
    if current_digit:
        digits.append(int(current_digit))
    
    return digits