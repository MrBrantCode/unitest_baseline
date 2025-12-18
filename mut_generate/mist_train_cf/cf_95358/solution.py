"""
QUESTION:
Write a function `extract_digits(s)` that takes a string `s` containing only digits and letters as input and returns a list of integers representing the digits in the same order as they appear in the string. The function should not use built-in functions or regular expressions, and its time complexity should be O(n), where n is the length of the input string.
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