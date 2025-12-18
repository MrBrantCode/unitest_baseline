"""
QUESTION:
Write a function called `alternate_case(s)` that takes a string `s` as input and returns a string with alternating casing, where alphabetic characters are converted to uppercase if their position is even and to lowercase if their position is odd, and non-alphabetic characters remain unchanged.
"""

def alternate_case(s):
    result = ""
    
    for i in range(len(s)):
        if s[i].isalpha():
            if i % 2 == 0:
                result += s[i].upper()
            else:
                result += s[i].lower()
        else:
            result += s[i]

    return result