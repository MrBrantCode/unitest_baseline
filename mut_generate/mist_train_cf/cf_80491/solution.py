"""
QUESTION:
Write a function `find_median(sorted_list)` that takes a sorted list of integers as input and returns the median of the list. The function should handle cases where the input list is empty, contains non-integer values, or is not a list. The median of a list is the middle value if the length is odd, or the average of the two middle values if the length is even.
"""

def find_median(sorted_list):
    # Checks if input is a list
    assert isinstance(sorted_list, list), "Input should be a list."
    # Checks if list is non-empty
    assert len(sorted_list) > 0, "List should be non-empty."
    # checks if all elements in the list are integers
    assert all(isinstance(i, int) for i in sorted_list), "List should only contain integers."
    
    sorted_list.sort() 
    list_length = len(sorted_list)

    if list_length % 2 == 0:
        # Return average of the two middle values
        return (sorted_list[(list_length)//2] + sorted_list[(list_length)//2 - 1])/2.0 
    else:
        # Return the middle value
        return sorted_list[(list_length-1)//2]