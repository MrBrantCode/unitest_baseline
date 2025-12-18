"""
QUESTION:
Create a function `filter_and_sort_strings` that takes a list of strings as input, filters out the strings that start with a vowel (a, e, i, o, or u), and returns a set of the remaining strings sorted in descending order based on their lengths. The function should have a time complexity of O(n log n).
"""

def filter_and_sort_strings(strings):
    """
    This function filters out strings that start with a vowel from the input list 
    and returns a set of the remaining strings sorted in descending order based on their lengths.
    
    Args:
    strings (list): A list of strings.
    
    Returns:
    set: A set of strings that do not start with a vowel, sorted in descending order by length.
    """
    # Convert list to set and filter strings that start with a vowel
    filtered_set = {string for string in strings if string[0].lower() not in ['a', 'e', 'i', 'o', 'u']}
    
    # Sort set in descending order based on string length
    sorted_set = sorted(filtered_set, key=lambda x: len(x), reverse=True)
    
    return set(sorted_set)