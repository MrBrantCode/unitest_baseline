"""
QUESTION:
Construct a function named `capitalize_string` that takes a string as input and returns the capitalized version of the string. The function should capitalize the first letter of each word, handle special characters by correctly capitalizing the first letter after each special character, and remove leading and trailing whitespace. The function should also handle multiple consecutive spaces between words and ensure that there is only a single space between words in the final capitalized string. The function should have a time complexity of O(n) and should not use any built-in string manipulation functions.
"""

def entance(string):
    string = string.strip()  
    result = []
    capitalize_next = True

    for char in string:
        if char.isalpha():
            if capitalize_next:
                result.append(char.upper())
                capitalize_next = False
            else:
                result.append(char.lower())
        elif char.isspace():
            if not capitalize_next and result[-1] != ' ':
                result.append(' ')
                capitalize_next = True
        else:
            result.append(char)
            capitalize_next = True

    return ''.join(result)