"""
QUESTION:
Create a function `capitalize_first_and_last` that takes a string `s` as input. The function should capitalize the first and last letter of each word in the string, while converting all other characters to lowercase.
"""

def capitalize_first_and_last(s):
    return ' '.join(word[0].upper() + word[1:-1].lower() + word[-1].upper() if len(word) > 1 else word.upper() for word in s.split())