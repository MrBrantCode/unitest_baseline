"""
QUESTION:
Create a function named `filter_by_character` that takes an array of strings (`str_arr`) and a single character (`char`) as parameters. The function should return a new array containing only the strings from `str_arr` that include the given `char`.
"""

def filter_by_character(str_arr, char):
    filtered_arr = []
    for string in str_arr:
        if char in string:
            filtered_arr.append(string)
    return filtered_arr