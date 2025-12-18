"""
QUESTION:
Create a function called `flatten` that takes two parameters: a two-dimensional array with unknown depths and an optional depth parameter. The function should return a one-dimensional array where all nested arrays are flattened up to the specified depth. If the depth parameter is not provided, it should default to -1, indicating that all depths should be flattened. The function should be able to handle various data types within the array.
"""

def flatten(lst, depth=-1):
    """
    Flattens a two-dimensional array up to a specified depth.

    Args:
        lst (list): The two-dimensional array to be flattened.
        depth (int, optional): The depth up to which the array should be flattened. Defaults to -1.

    Returns:
        list: A one-dimensional array where all nested arrays are flattened up to the specified depth.
    """
    if not isinstance(lst, list) or depth == 0:
        return [lst]
        
    result = []
    for item in lst:
        result.extend(flatten(item, depth-1))

    return result