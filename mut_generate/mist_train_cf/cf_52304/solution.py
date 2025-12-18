"""
QUESTION:
Write a function named `complex_sort` that takes a list of elements of different data types as input and returns a sorted list. The sorting priority should be: integers (sorted in descending order), floats (sorted in ascending order), strings (sorted in alphabetical order), and then others (sorted based on their string representation, alphabetical order).
"""

def complex_sort(lst):
    """
    Sorts a list of elements of different data types.

    The sorting priority is:
    - Integers (sorted in descending order)
    - Floats (sorted in ascending order)
    - Strings (sorted in alphabetical order)
    - Others (sorted based on their string representation, alphabetical order)

    Args:
        lst (list): A list of elements of different data types.

    Returns:
        list: A sorted list.
    """

    types = {int: [], float: [], str: [], 'other': []}
    
    for el in lst:
        if type(el) == int:
            types[int].append(el)
        elif type(el) == float:
            types[float].append(el)
        elif type(el) == str:
            types[str].append(el)
        else:
            types['other'].append(el)
    
    types[int] = sorted(types[int], reverse=True)
    types[float] = sorted(types[float])
    types[str] = sorted(types[str])
    types['other'] = sorted(types['other'], key=str)
    
    return types[int] + types[float] + types[str] + types['other']