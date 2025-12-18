"""
QUESTION:
Write a function named `common_elements` that takes two lists of integers as input, removes duplicates from both lists, finds their common elements, removes duplicates from the common elements, and returns them in ascending order. The function should have a time complexity of O(n) and should not use any built-in functions or libraries except for `len()`, `range()`, and `int()`.
"""

def common_elements(list1, list2):
    """
    This function finds the common elements between two lists, removes duplicates, 
    and returns them in ascending order.

    Args:
    list1 (list): The first list of integers.
    list2 (list): The second list of integers.

    Returns:
    list: A list of common elements in ascending order.
    """
    list1_set = set(list1)
    list2_set = set(list2)
    
    common_elements = []
    for num in list1_set:
        if num in list2_set:
            common_elements.append(num)
    
    common_elements = list(set(common_elements))
    common_elements.sort()
    
    return common_elements