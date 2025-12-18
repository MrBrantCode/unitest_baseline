"""
QUESTION:
Create a function named `reverse_capitalization_substitute` that takes a string as input and returns a string where all alphabetic characters have their capitalization reversed, odd digits are replaced with the next even number, and all other characters are duplicated. The function should handle both uppercase and lowercase letters, and it should work for strings containing any combination of letters, digits, and special characters.
"""

def reverse_capitalization_substitute(string: str) -> str:
    result = ''
    for char in string:
        if char.isalpha():
            if char.isupper():
                result += char.lower()
            else:
                result += char.upper()
        elif char.isdigit():
            if int(char) % 2 == 1:
                result += str(int(char) + 1)
            else:
                result += char
        else:
            result += char*2
    return result