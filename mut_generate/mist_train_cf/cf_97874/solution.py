"""
QUESTION:
Create a function `sort_and_remove_duplicates` that takes a list of strings as input and returns a concatenated string of the sorted and deduplicated list. The function should also handle the following cases: 

- If the input list is empty, it should return a custom error message specified by an optional parameter `empty_list`.
- If a string in the list contains special characters, it should replace them with a blank space.
- If the list contains only strings with special characters, it should return an error message "Error: List contains only special characters".
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