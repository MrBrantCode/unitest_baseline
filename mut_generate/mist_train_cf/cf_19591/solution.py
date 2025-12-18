"""
QUESTION:
Implement a function named `rotate_array` that takes two parameters: `arr` (a list of integers with a length of at least 2) and `rotation` (a positive integer). The function should modify the original array `arr` by rotating it `rotation` number of times in a clockwise direction. The rotation should be performed in-place and have a time complexity of O(n), where n is the length of the array.
"""

def rotate_array(arr, rotation):
    """
    Rotate the given array in a clockwise direction by the specified number of times.
    
    Args:
        arr (list): A list of integers with a length of at least 2.
        rotation (int): A positive integer representing the number of times to rotate the array.
    
    Returns:
        None: The array is modified in-place.
    """
    
    # Calculate the effective rotation value
    effective_rotation = rotation % len(arr)
    
    # If the effective rotation is 0, return early
    if effective_rotation == 0:
        return
    
    # Reverse the entire array
    arr.reverse()
    
    # Reverse the first effective_rotation elements
    arr[:effective_rotation] = arr[:effective_rotation][::-1]
    
    # Reverse the remaining elements
    arr[effective_rotation:] = arr[effective_rotation:][::-1]