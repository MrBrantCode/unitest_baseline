"""
QUESTION:
You will be given a vector of strings. You must sort it alphabetically (case-sensitive, and based on the ASCII values of the chars) and then return the first value.

The returned value must be a string, and have `"***"` between each of its letters.

You should not remove or add elements from/to the array.
"""

def sort_and_format_first_string(lst):
    # Sort the list alphabetically (case-sensitive)
    sorted_lst = sorted(lst)
    
    # Get the first string from the sorted list
    first_string = sorted_lst[0]
    
    # Join the characters of the first string with "***"
    formatted_string = '***'.join(first_string)
    
    return formatted_string