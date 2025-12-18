"""
QUESTION:
Write a function `sum_unique_elements` that takes a list of integers as input, returns the sum of unique elements, and modifies the original list to remove any duplicate values. The function should achieve this with a time complexity of O(n) and a space complexity of O(n), where n is the length of the list.
"""

def sum_unique_elements(lst):
    """
    This function calculates the sum of unique elements in a list and removes duplicates from the original list.
    
    Args:
        lst (list): A list of integers.
    
    Returns:
        int: The sum of unique elements.
    """
    unique_elements = set()
    sum_of_unique_elements = 0
    
    for i in range(len(lst) - 1, -1, -1):
        if lst[i] not in unique_elements:
            unique_elements.add(lst[i])
            sum_of_unique_elements += lst[i]
        else:
            lst.pop(i)
    
    return sum_of_unique_elements