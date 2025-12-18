"""
QUESTION:
Remove duplicates from a list of strings and sort the remaining strings in descending order based on the length of the string. If two or more strings have the same length, sort them in alphabetical order. The function should handle lists of up to 1 million strings, each with a length of up to 100 characters. Implement the `remove_duplicates_sort` function to achieve this.
"""

def remove_duplicates_sort(strings):
    # Remove duplicates
    unique_strings = list(set(strings))
    
    # Sort strings based on length in descending order and remove empty strings
    sorted_strings = sorted([string for string in unique_strings if string != ""], key=lambda x: (-len(x), x))
    
    return sorted_strings