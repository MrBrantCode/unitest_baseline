"""
QUESTION:
Write a function `find_elements` that takes a list of strings as input and returns a list of unique strings from the input list where each string ends with 's'. The output list should be sorted in ascending order, contain no duplicates, and the function should have a time complexity of O(n), where n is the length of the input list.
"""

def find_elements(arr):
    """Returns a list of unique strings from the input list where each string ends with 's'.
    
    Args:
        arr (list): A list of strings.
    
    Returns:
        list: A sorted list of unique strings that end with 's'.
    """
    unique_elements = set()
    
    for element in arr:
        if element[-1] == 's':
            unique_elements.add(element)
    
    sorted_elements = sorted(unique_elements)
    return sorted_elements