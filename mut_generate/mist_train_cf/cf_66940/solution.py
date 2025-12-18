"""
QUESTION:
Write a function `find_overlap` that takes two lists of integers as input and returns the maximum overlap between the two lists. The maximum overlap is defined as the number of elements that are common to both lists. Assume that the input lists are not empty and do not contain duplicate elements.
"""

def find_overlap(data1, data2):
    """
    This function finds the maximum overlap between two lists of integers.
    
    Args:
        data1 (list): The first list of integers.
        data2 (list): The second list of integers.
    
    Returns:
        int: The maximum overlap between the two lists, defined as the number of elements that are common to both lists.
    """
    return len(set(data1) & set(data2))