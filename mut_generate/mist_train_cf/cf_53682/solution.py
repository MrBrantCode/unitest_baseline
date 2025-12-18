"""
QUESTION:
Create a function called `common` that takes two lists of integers as input and returns a new list containing their unique common elements in ascending order. The function should exclude any duplicate values and the output should be sorted.
"""

def common_elements(l1, l2):
    """
    This function takes two lists of integers as input and returns a new list containing their unique common elements in ascending order.
    
    Parameters:
    l1 (list): The first list of integers.
    l2 (list): The second list of integers.
    
    Returns:
    list: A new list containing the unique common elements of l1 and l2 in ascending order.
    """
    # Convert the lists to sets for efficient lookup and to remove duplicates
    set1 = set(l1)
    set2 = set(l2)
    
    # Find the intersection of the two sets (i.e., the common elements)
    common = set1.intersection(set2)
    
    # Convert the set of common elements back to a list and sort it
    result = sorted(list(common))
    
    return result