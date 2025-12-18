"""
QUESTION:
Write a function `merge_nested_list` that takes a nested list of strings as input, where each sublist contains individual words. The function should return a single string where the words in each sublist are joined by a space, and the resulting strings are also joined by a space. The function should not take any additional arguments other than the nested list.
"""

def merge_nested_list(nested_list):
    """
    This function takes a nested list of strings as input, 
    where each sublist contains individual words. It returns 
    a single string where the words in each sublist are joined 
    by a space, and the resulting strings are also joined by a space.

    Args:
        nested_list (list): A nested list of strings.

    Returns:
        str: A single string with all the words from the nested list.
    """
    # joining words in each sublist
    merged_sublists = [' '.join(item) for item in nested_list]
    
    # concatenate all the strings into one
    return ' '.join(merged_sublists)