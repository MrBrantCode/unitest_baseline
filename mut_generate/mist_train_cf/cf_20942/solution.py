"""
QUESTION:
Find the time complexity of the function `find_value_at_index` that retrieves the value at a given index from a multidimensional unordered array, possibly containing duplicate values. The function must handle arrays of any size and dimension. Assume the array is represented as a nested list in Python.
"""

def find_value_at_index(array, index):
    """
    Retrieves the value at a given index from a multidimensional unordered array.
    
    Args:
        array (list): A multidimensional unordered array represented as a nested list.
        index (tuple): A tuple representing the index of the value to be retrieved.
        
    Returns:
        The value at the specified index, or None if the index is out of bounds.
    """
    def recursive_search(array, index):
        if not index:
            return array
        return recursive_search(array[index[0]], index[1:])
    
    try:
        return recursive_search(array, index)
    except (IndexError, TypeError):
        return None