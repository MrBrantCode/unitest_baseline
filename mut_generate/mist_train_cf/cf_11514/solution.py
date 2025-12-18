"""
QUESTION:
Create a function `remove_duplicates` that takes a list of mixed data types (integers and strings) as input and returns a new list with duplicate elements removed. Two elements are considered duplicates if they have the same value and data type. The function should preserve the original order of elements in the list.
"""

def remove_duplicates(input_list):
    """
    Removes duplicate elements from a list containing a mixture of integers and strings.
    
    Args:
    input_list (list): A list of mixed data types (integers and strings).
    
    Returns:
    list: A new list with duplicate elements removed, preserving the original order.
    """
    unique_set = set()
    unique_list = []

    for element in input_list:
        if element not in unique_set:
            unique_set.add(element)
            unique_list.append(element)

    return unique_list