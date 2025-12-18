"""
QUESTION:
Implement a function `amplified_case_inversion_and_alteration` that takes a string as input and returns a modified string where all alphabetic letters have their case reversed, all odd digits are replaced with their immediately succeeding even numeral, and all non-alphanumeric characters are duplicated.
"""

def amplified_case_inversion_and_alteration(string: str) -> str:
    result = ""
    for char in string:
        if char.isalpha():
            if char.islower():
                result += char.upper()
            else:
                result += char.lower()
        elif char.isdigit():
            digit = int(char)
            if digit % 2 == 1:
                result += str(digit + 1)
            else:
                result += char
        else:
            result += char * 2
    return result