"""
QUESTION:
Write a function called `reverse_slice` that takes a list and an integer `n` as input, reverses the elements of the list up to index `n` (inclusive), and returns the reversed portion. The function should not use any built-in list manipulation functions or methods and should have a time complexity of O(n), where n is the length of the list.
"""

def reverse_slice(lst, n):
    """
    Reverses the elements of the list up to index n (inclusive) and returns the reversed portion.
    
    Args:
    lst (list): The input list.
    n (int): The index up to which the list should be reversed.
    
    Returns:
    list: The reversed portion of the list.
    """
    start_index = 0
    end_index = n
    
    while start_index < end_index:
        # Swap the elements at start_index and end_index
        temp = lst[start_index]
        lst[start_index] = lst[end_index]
        lst[end_index] = temp
        
        # Move to the next elements
        start_index += 1
        end_index -= 1
    
    return lst[:n+1]