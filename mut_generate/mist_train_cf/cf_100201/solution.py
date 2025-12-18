"""
QUESTION:
Write a function named sort_and_remove_duplicates that sorts a list of strings alphabetically and removes duplicates. The function should also meet the following requirements:

- Concatenate all the strings in the list and return the resulting string.
- Include an optional parameter to handle cases where the input list is empty.
- Handle cases where the list contains strings with special characters (such as "!", "&", "(", etc.) by replacing them with a blank space. If the list contains only strings with special characters, return an error message instead of the concatenated string.
"""

def sort_and_remove_duplicates(lst, empty_list=[]):
    """
    Sorts a list of strings alphabetically and removes duplicates.
    """
    if not lst:
        return empty_list
    
    str_list = []
    for s in lst:
        if all(c.isalpha() or c.isspace() for c in s):
            str_list.append(s)
        else:
            s = ''.join(c if c.isalpha() or c.isspace() else ' ' for c in s)
            if all(c.isspace() for c in s):
                return "Error: List contains only special characters"
            str_list.append(s)
    
    sorted_str_list = sorted(list(set(str_list)))
    concatenated_str = ''.join(sorted_str_list)
    return concatenated_str