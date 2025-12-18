"""
QUESTION:
Write a function called `sort_strings` that takes a list of mixed variable types as input, including integers, floating-point numbers, strings, and other non-comparable data types such as lists and dictionaries. The function should sort the strings in the list alphabetically while maintaining their original relative positions and the positions of all non-string elements. The function should return the modified list.
"""

def sort_strings(mixed_list):
    # Filter out strings from list
    strings = [element for element in mixed_list if isinstance(element, str)]
    # Sort list of strings
    strings.sort()

    # Insert sorted strings back into list
    sorted_list = []
    i = 0  # index for sorted strings

    for element in mixed_list:
        if isinstance(element, str):
            sorted_list.append(strings[i])
            i += 1
        else:
            sorted_list.append(element)

    return sorted_list