"""
QUESTION:
Implement a function named `capitalize_string` that takes a string of any length as input and returns its capitalized version. The function should capitalize the first letter of each word, handle special characters by correctly capitalizing the first letter after each special character, and remove any leading or trailing whitespace. The function should also ensure that there is only a single space between words in the final capitalized string. The time complexity of the function should be O(n), where n is the length of the input string, and it should not use any built-in string manipulation functions.
"""

def capitalize_string(string):
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