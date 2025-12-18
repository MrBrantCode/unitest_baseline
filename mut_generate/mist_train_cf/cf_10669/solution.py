"""
QUESTION:
Create a function called `sort_list` that takes a set `s` as input and returns a sorted list. The input set `s` can contain a mix of data types, including strings and integers, and may include duplicates and empty strings. The output list should only include unique, non-empty strings and integers, sorted alphabetically.
"""

def sort_list(s):
    # Create a new list to store valid elements
    valid_elements = []
    
    # Iterate over the set
    for element in s:
        # Check if the element is a string or an integer (excluding empty strings)
        if isinstance(element, str) and element != "" or isinstance(element, int):
            valid_elements.append(str(element))
    
    # Sort the list alphabetically and remove duplicates
    final_list = sorted(set(valid_elements))
    
    return final_list