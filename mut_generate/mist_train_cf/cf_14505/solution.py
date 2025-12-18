"""
QUESTION:
Implement the function `insertion_sort_descending(arr)` to sort the given array in descending order using the insertion sort algorithm. The array can contain duplicate elements.
"""

def insertion_sort_descending(arr):
    """
    Sorts the given array in descending order using the insertion sort algorithm.
    
    Args:
    arr (list): The input array to be sorted.
    
    Returns:
    list: The sorted array in descending order.
    """
    
    # Start from the second element (index 1) of the array.
    for i in range(1, len(arr)):
        
        # Set the current element as the key.
        key = arr[i]
        
        # Initialize a variable j as the index of the previous element.
        j = i - 1
        
        # While j is greater than or equal to 0 and the element at index j is less than the key:
        while j >= 0 and arr[j] < key:
            
            # Move the element at index j one position ahead.
            arr[j + 1] = arr[j]
            
            # Decrement j by 1.
            j -= 1
        
        # Place the key at its correct position within the sorted section of the array.
        arr[j + 1] = key
    
    # Return the sorted array in descending order.
    return arr