"""
QUESTION:
Design a function named `shift_zeros_to_end` that takes a list as input and shifts all zero values to the end of the list while maintaining the relative order of the non-zero elements. The function should also be able to handle nested lists and shift all zero values in the nested lists to the end of their respective lists. Do not use any built-in Python functions or libraries to directly solve the problem.
"""

def shift_zeros_to_end(lst):
    """
    Shifts all zero values to the end of the list while maintaining the relative order of the non-zero elements.
    Handles nested lists by recursively shifting zero values in the nested lists to the end of their respective lists.
    
    Args:
        lst (list): The input list that may contain nested lists and zero values.
    
    Returns:
        list: The input list with all zero values shifted to the end.
    """
    for i in range(len(lst)):
        if type(lst[i]) is list:
            shift_zeros_to_end(lst[i])
        else:
            if lst[i] == 0:
                lst.append(lst.pop(i))
    return lst