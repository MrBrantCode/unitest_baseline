"""
QUESTION:
Write a function `concatenateStrings` that takes two strings, `string1` and `string2`, as input. The function should return a concatenated string that is in all uppercase characters and contains only alphabetical characters. The function should also enforce the following restrictions: `string1` should have a maximum length of 10 characters, and `string2` should have a minimum length of 5 characters.
"""

def concatenateStrings(string1, string2):
    result = ""
    
    if not string1 or not string2 or len(string1) > 10 or len(string2) < 5:
        return "Invalid input strings."
    
    string1 = string1.upper()
    string2 = string2.upper()
    
    for char in string1:
        if char.isalpha() and len(result) < 10:
            result += char
    
    for char in string2:
        if char.isalpha() and len(result) < 15:
            result += char
    
    return result