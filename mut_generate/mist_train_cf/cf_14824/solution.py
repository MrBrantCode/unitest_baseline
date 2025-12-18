"""
QUESTION:
Write a function `check_alphabet_order(s)` that checks if a given string contains all the alphabets in the correct order, with the alphabets appearing consecutively and in the same order as they do in the English alphabet. The function should be case-insensitive.
"""

def check_alphabet_order(s):
    s = s.lower()
    expected_char = 'a'
    for char in s:
        if char == expected_char:
            expected_char = chr(ord(expected_char) + 1)
        if expected_char == '{':
            return True
    return False