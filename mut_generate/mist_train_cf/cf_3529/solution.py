"""
QUESTION:
Write a function `find_positions(y, x)` that finds the positions of all occurrences of an element `x` in a list `y`. The function should handle cases where `y` contains nested lists and `x` can be a nested list. The function should return a list of positions where `x` is found. If `x` is not found, the function should return an empty list. The positions should be represented as a list of indices, where each index corresponds to the nested level of the list.
"""

def find_positions(y, x):
    """
    Finds the positions of all occurrences of an element x in a list y.
    
    Args:
        y (list): The list to search in.
        x (element): The element to search for.
    
    Returns:
        list: A list of positions where x is found. If x is not found, an empty list is returned.
    """
    positions = []
    for i in range(len(y)):
        if type(y[i]) == list:
            nested_positions = find_positions(y[i], x)
            if nested_positions:
                for position in nested_positions:
                    positions.append([i] + position)
        elif y[i] == x:
            positions.append([i])
    return positions