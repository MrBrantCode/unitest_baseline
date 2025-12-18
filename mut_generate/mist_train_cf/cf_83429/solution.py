"""
QUESTION:
Write a function named `map_elements` that takes two lists `x` and `y` as input and returns two dictionaries. The first dictionary maps the occurrence counts of each element from list `x` and list `y`. The second dictionary maps the occurrence counts of the intersection of elements from list `x` in list `y`. The function should achieve this in a time complexity of O(n).
"""

def map_elements(x, y):
    """
    Maps the occurrence counts of each element from list x and list y.
    Maps the occurrence counts of the intersection of elements from list x in list y.

    Args:
        x (list): The first list of elements.
        y (list): The second list of elements.

    Returns:
        tuple: A tuple of two dictionaries. The first dictionary maps the occurrence counts of each element from list x.
               The second dictionary maps the occurrence counts of the intersection of elements from list x in list y.
    """
    dict_x = {}
    dict_xy = {}
    
    # Mapping the occurrence counts of each element in list x
    for i in x:
        if i not in dict_x:
            dict_x[i] = 1
        else:
            dict_x[i] += 1

    # Mapping the occurrence counts of the intersection of elements from lists x and y
    for i in y:
        if i in dict_x:
            if i not in dict_xy:
                dict_xy[i] = 1
            else:
                dict_xy[i] += 1
                
    return dict_x, dict_xy