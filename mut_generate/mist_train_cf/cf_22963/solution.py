"""
QUESTION:
Write a function `capitalize_first_letter` that takes a string as an argument and returns the same string with the first letter capitalized. The function should also capitalize the first letter after each punctuation mark ('.', '!', '?', ':') if it is not followed by a space. The function should have a time complexity of O(n), where n is the length of the string.
"""

def capitalize_first_letter(string):
    if len(string) == 0:
        return ""

    # Capitalize first letter
    result = string[0].upper()

    # Loop through the string starting from the second character
    for i in range(1, len(string)):
        # If the previous character is a punctuation mark
        if string[i-1] in ['.', '!', '?', ':']:
            # If the current character is not a space, capitalize it
            if string[i] != ' ':
                result += string[i].upper()
            else:
                result += string[i]
        else:
            result += string[i]

    return result