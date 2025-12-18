"""
QUESTION:
Create a function `sort_negatives` that takes a list of integers as input, sorts the negative integers in ascending order, and returns the original list with the sorted negative integers. The non-negative integers in the list should remain in their original positions. The input list can contain both positive and negative integers.
"""

def sort_negatives(lst):
    """
    This function takes a list of integers as input, sorts the negative integers 
    in ascending order, and returns the original list with the sorted negative integers.
    
    Parameters:
    lst (list): A list of integers containing both positive and negative numbers.
    
    Returns:
    list: The original list with the negative integers sorted in ascending order.
    """
    
    # Create a new list containing all negative numbers from the input list, sorted in ascending order
    negatives = sorted([i for i in lst if i < 0])
    
    # Initialize an index to track the current negative number to be replaced
    neg_index = 0
    
    # Iterate over the input list
    for i in range(len(lst)):
        # Check if the current number is negative
        if lst[i] < 0:
            # Replace the negative number with the next negative number from the sorted list
            lst[i] = negatives[neg_index]
            # Increment the index to point to the next negative number
            neg_index += 1
    
    # Return the modified list with sorted negative integers
    return lst