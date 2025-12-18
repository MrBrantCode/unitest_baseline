"""
QUESTION:
Write a function `move_zeroes_to_end` that takes a list of integers as input and returns a new list with all zeroes moved to the end, while maintaining the relative order of non-zero elements.
"""

def move_zeroes_to_end(array):
    """
    This function takes a list of numbers as input, 
    moves all the zeroes to the end 
    and returns the updated list.
    """
    # count the number of zeros
    num_zeros = array.count(0)
    
    # remove all zeros from the list
    array = [num for num in array if num != 0]
    
    # extend the list by the number of zeros
    array.extend([0]*num_zeros)
    
    return array