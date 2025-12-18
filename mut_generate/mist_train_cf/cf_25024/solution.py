"""
QUESTION:
Write a function `nestedListSum` that calculates the sum of all elements in a nested list. The input is a list that contains one or more lists, each of which may contain integers. Return the total sum of all integers in the nested list.
"""

def nestedListSum(nested_list):
    """
    This function calculates the sum of all elements in a nested list.
    
    Args:
        nested_list (list): A list that contains one or more lists, each of which may contain integers.
    
    Returns:
        int: The total sum of all integers in the nested list.
    """
    total = 0
    for sub_list in nested_list:
        if isinstance(sub_list, list):
            total += nestedListSum(sub_list)
        else:
            total += sub_list
    return total