"""
QUESTION:
Develop a function named `expand_list` that creates a new multidimensional list exactly twice as expansive as the original list. The input list can contain both integers and nested lists. Duplicate each element in the original list, including nested lists, and include them in the new list.
"""

def expand_list(original_list):
    """
    Creates a new multidimensional list exactly twice as expansive as the original list.
    
    Args:
    original_list: A list containing integers and nested lists.
    
    Returns:
    A new list with each element from the original list duplicated.
    """
    expanded_list = []
    for ele in original_list:
        if isinstance(ele, list):
            expanded_list.append(expand_list(ele))
            expanded_list.append(expand_list(ele))
        else:
            expanded_list.append(ele)
            expanded_list.append(ele)
    return expanded_list