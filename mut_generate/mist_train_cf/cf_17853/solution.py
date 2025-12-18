"""
QUESTION:
Create a function `is_valid_number` that takes a string as input and returns a boolean value. The input string is considered a valid number if it meets the following conditions: 
- it is at least 5 characters long, 
- it consists of only digits, alphabetic characters, and special characters, 
- it starts with a letter, 
- it ends with a digit, 
- and it contains at least one special character in between.
"""

def is_valid_number(s):
    if not s:
        return False

    if not (s[0].isalpha() and s[-1].isdigit()):
        return False

    special_char_count = 0
    for char in s[1:-1]:
        if not char.isalpha() and not char.isdigit():
            special_char_count += 1

    if special_char_count < 1 or len(s) < 5:
        return False

    return True