"""
QUESTION:
Create a function `replace_characters(string)` that takes a string of up to 100 characters and returns the string with all alphabetic characters replaced by their next consecutive character. The function should handle both uppercase and lowercase letters separately, wrapping around from 'z' to 'a' or 'Z' to 'A' when necessary, and maintain the original capitalization of the characters. Non-alphabetic characters should be ignored and added to the result string as is.
"""

def replace_characters(string):
    result = ''
    for char in string:
        if char.isalpha():
            if char.islower():
                if char == 'z':
                    result += 'a'
                else:
                    result += chr(ord(char) + 1)
            else:
                if char == 'Z':
                    result += 'A'
                else:
                    result += chr(ord(char) + 1)
        else:
            result += char
    return result