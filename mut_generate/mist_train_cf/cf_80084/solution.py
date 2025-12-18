"""
QUESTION:
Implement a function to create an n-dimensional sparse array filled with zeros using a custom implementation. The function should allow for setting and getting values at specific coordinates in the array, with a default value of 0 for unset coordinates. The function should be efficient in terms of memory usage, using a nested dictionary to store only the non-zero values. The input will be the coordinates (x, y, z, w, ..., n) and the value to be set or retrieved. The output should be the value at the specified coordinates or the updated array after setting a new value.
"""

def create_sparse_array(coordinates, value=None):
    """
    Creates an n-dimensional sparse array filled with zeros.
    
    Args:
    coordinates (tuple): A tuple of coordinates (x, y, z, w, ..., n).
    value (int, optional): The value to be set at the specified coordinates. Defaults to None.
    
    Returns:
    int or dict: The value at the specified coordinates if value is None, otherwise the updated array.
    """
    data = {}
    
    def _get_element(coordinates, dictionary):
        if len(coordinates) == 1:
            return dictionary.get(coordinates[0], 0)
        if coordinates[0] not in dictionary:
            return 0
        return _get_element(coordinates[1:], dictionary[coordinates[0]])
    
    def _set_element(coordinates, value, dictionary):
        if len(coordinates) == 1:
            dictionary[coordinates[0]] = value
            return
        if coordinates[0] not in dictionary:
            dictionary[coordinates[0]] = {}
        _set_element(coordinates[1:], value, dictionary[coordinates[0]])
    
    if value is not None:
        _set_element(coordinates, value, data)
        return data
    else:
        return _get_element(coordinates, data)