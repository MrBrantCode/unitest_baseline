"""
QUESTION:
Create a function `replace_characters` that takes a string as input and returns a new string where each alphabetic character is replaced by the next consecutive character, maintaining the original capitalization. Non-alphabetic characters should be ignored and remain unchanged. The function should handle wrap-around cases where 'z' is replaced by 'a' and 'Z' is replaced by 'A'.
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