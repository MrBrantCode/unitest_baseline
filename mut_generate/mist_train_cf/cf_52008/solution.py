"""
QUESTION:
Develop a function `average` that calculates the average length of all string elements within a list that can contain strings, lists, and tuples. The function should not use built-in average functions and must handle unbalanced data without relying on helper functions. A custom comparison function `cmp_func` should be provided for comparing string entities, although it's not used in the average calculation.
"""

def average(l: list, cmp_func: callable):
    """
    This function calculates the average length of all string elements within a list 
    that can contain strings, lists, and tuples.
    
    Args:
    l (list): A list containing strings, lists, and tuples.
    cmp_func (callable): A comparison function (not used in this implementation).
    
    Returns:
    float or None: The average length of all string elements. Returns None if there are no string elements.
    """
    total_length = 0 
    total_items = 0 
    for item in l:
        if type(item) == str:
            total_length += len(item)
            total_items += 1
        elif type(item) in [list, tuple]:
            for i in item:
                if type(i) == str:
                    total_length += len(i)
                    total_items += 1
    return total_length / total_items if total_items else None