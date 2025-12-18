"""
QUESTION:
Design a function `find_longest_string_index` that takes a list of strings as input and returns the index of the longest string in the list. The function should have a time complexity of O(n), where n is the length of the list, and a space complexity of O(1). The function should be able to handle cases where the longest string is at the end of the list and where all strings have the same length.
"""

def find_longest_string_index(strings):
    """
    This function finds the index of the longest string in a given list of strings.
    
    Args:
        strings (list): A list of strings.
    
    Returns:
        int: The index of the longest string in the list.
    """
    max_length = 0
    max_index = -1
    for i in range(len(strings)):
        if len(strings[i]) > max_length:
            max_length = len(strings[i])
            max_index = i
        elif len(strings[i]) == max_length and max_index == -1:
            max_index = i
    return max_index