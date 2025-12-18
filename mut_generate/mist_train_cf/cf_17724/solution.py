"""
QUESTION:
Write a function named `sort_strings` that sorts all strings in a given list alphabetically and removes any duplicate strings. The function should have a time complexity of O(nlogn) and a space complexity of O(n). The input will be a list of strings, and the output should be a list of sorted, unique strings.
"""

def sort_strings(strings):
    """
    Sorts all strings in a given list alphabetically and removes any duplicate strings.
    
    Args:
    strings (list): A list of strings.
    
    Returns:
    list: A list of sorted, unique strings.
    """
    return sorted(set(strings))