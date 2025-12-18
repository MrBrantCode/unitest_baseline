"""
QUESTION:
Create a function called `alternate_case(s)` that takes a string `s` as input and returns a new string where each alphabetic character's case is alternated between upper and lower case, while non-alphabetic characters remain unchanged, starting with upper case for the first alphabetic character.
"""

def alternate_case(s):
    result = ""
    upper_case = True

    for char in s:
        if char.isalpha():
            if upper_case:
                result += char.upper()
            else:
                result += char.lower()
            upper_case = not upper_case
        else:
            result += char

    return result