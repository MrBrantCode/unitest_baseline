"""
QUESTION:
Write a function `strings_starting_with_c` that takes a list of strings as input and returns a list of all strings that start with the character 'c'. The function must have a time complexity of O(n), where n is the total number of characters in all the strings combined.
"""

def strings_starting_with_c(list_strings):
    result = []
    for string in list_strings:
        if string and string[0].lower() == 'c':
            result.append(string)
    return result