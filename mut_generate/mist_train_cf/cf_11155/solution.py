"""
QUESTION:
Create a function called `concatenate_strings` that takes two parameters, `str1` and `str2`, both of which are strings. The function should return a new string that contains all characters from `str1` and `str2` in alphabetical order.
"""

def concatenate_strings(str1, str2):
    # Concatenate the two strings
    result = str1 + str2

    # Convert the result into a list of characters
    char_list = list(result)

    # Sort the characters in alphabetical order
    char_list.sort()

    # Convert the sorted list back into a string
    sorted_str = ''.join(char_list)

    return sorted_str