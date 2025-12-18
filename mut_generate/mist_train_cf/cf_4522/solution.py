"""
QUESTION:
Write a function named `move_zeros_to_end` that takes in an array of integers as input. The function should move all the zeros to the end of the array while maintaining the order of the non-zero elements, and return the modified array. The function must meet the following requirements: handle up to 10^5 elements, include both positive and negative integers, allow duplicates, have a time complexity of O(n), and have a space complexity of O(1).
"""

def move_zeros_to_end(arr):
    """
    Move all zeros to the end of the array while maintaining the order of non-zero elements.

    Args:
        arr (list): A list of integers.

    Returns:
        list: The modified list with all zeros moved to the end.
    """
    j = 0  # Pointer to keep track of the index where the next non-zero element should be placed.
    
    # Iterate through the array.
    for i in range(len(arr)):
        # If the element is non-zero, swap it with the element at index j and increment j by 1.
        if arr[i] != 0:
            arr[j], arr[i] = arr[i], arr[j]
            j += 1
    
    # After the iteration, all non-zero elements will be placed before the index j, and all remaining elements after index j will be zeros.
    # No need to fill the remaining elements after index j with zeros as they are already zeros.
    
    return arr