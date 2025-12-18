"""
QUESTION:
Write a function `invert_case_alter(string: str) -> str` that takes a string as input and returns a modified string where all alphabetic characters have their case inverted (lowercase becomes uppercase and vice versa), all odd digits are replaced with the next even digit, and all non-alphanumeric characters are duplicated.
"""

def invert_case_alter(string: str) -> str:
    new_string = ''
    for char in string:
        if char.isalpha():
            new_string += char.lower() if char.isupper() else char.upper()
        elif char.isdigit():
            new_digit = int(char)+1 if int(char) % 2 != 0 else int(char)
            new_string += str(new_digit)
        else:
            new_string += char*2
    return new_string