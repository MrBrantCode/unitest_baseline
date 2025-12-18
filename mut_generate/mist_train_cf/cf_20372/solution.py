"""
QUESTION:
Create a function `copy_array` that manually copies an array of integers to a new array without using any built-in array functions or methods. The array size is in the range of 10^6 to 10^7. The function should optimize the process to minimize the time complexity.
"""

def copy_array(original_array):
    """
    Manually copies an array of integers to a new array without using any built-in array functions or methods.
    
    Args:
        original_array (list): The original array of integers to be copied.
    
    Returns:
        list: A new array containing the copied elements from the original array.
    """
    
    # Preallocate the new array with the same size as the original array
    copied_array = [0] * len(original_array)
    
    # Iterate through each index of the original array
    for i in range(len(original_array)):
        # Copy the element at index 'i' to the new array at the same index
        copied_array[i] = original_array[i]
    
    return copied_array