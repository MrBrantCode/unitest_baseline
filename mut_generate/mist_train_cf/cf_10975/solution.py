"""
QUESTION:
Create a function named custom_sort that takes a list of mixed data types (integers and strings) as input and returns a sorted list. The integers should be sorted in ascending order, followed by the strings in lexicographic order. In case of multiple integers or strings with the same value, their original order should be maintained.
"""

def custom_sort(lst):
    """
    Sorts a list of mixed data types (integers and strings). 
    Integers are sorted in ascending order, followed by strings in lexicographic order.
    
    Args:
        lst (list): A list of mixed data types.
    
    Returns:
        list: A sorted list.
    """
    # Separate integers and strings
    ints = [x for x in lst if isinstance(x, int)]
    strs = [x for x in lst if isinstance(x, str)]
    
    # Sort integers in ascending order and maintain original order of equal elements
    ints.sort()
    
    # Sort strings in lexicographic order and maintain original order of equal elements
    strs.sort()
    
    # Combine the sorted lists
    return ints + strs