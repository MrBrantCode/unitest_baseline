"""
QUESTION:
Write a function called `remove_sixes` that takes an array of integers as input and returns a new array with all elements having the value 6 removed. The function should return a new array, not modify the original array, and should not use any built-in array filtering methods.
"""

def remove_sixes(arr):
    """
    This function takes an array of integers as input and returns a new array with all elements having the value 6 removed.
    
    Parameters:
    arr (list): The input array of integers.
    
    Returns:
    list: A new array with all elements having the value 6 removed.
    """
    count = 0
    # Count the number of occurrences of the element 6
    for i in range(len(arr)):
        if arr[i] == 6:
            count += 1

    # Create a new array with a size equal to the original array minus the count of occurrences of 6
    new_arr = [0] * (len(arr) - count)
    new_index = 0

    # Iterate through the original array, copying all elements except for the ones with the value 6 to the new array
    for i in range(len(arr)):
        if arr[i] != 6:
            new_arr[new_index] = arr[i]
            new_index += 1

    # Return the new array as the resulting array
    return new_arr