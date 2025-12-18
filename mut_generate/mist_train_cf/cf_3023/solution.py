"""
QUESTION:
Create a function named `is_sorted` that determines whether a given array is sorted in either ascending or descending order. The function should have a time complexity of O(n), where n is the number of elements in the array. It should not use comparison operators (such as >, <, ==) to compare array elements; only arithmetic operations and bitwise operators are allowed.
"""

def is_sorted(array):
    length = len(array)
    if length <= 1:
        return True
    
    difference = array[length-1] - array[0]
    if difference >= 0:
        is_ascending = True
    else:
        is_ascending = False
    
    for i in range(1, length):
        difference = array[i] - array[i-1]
        if (difference > 0 and not is_ascending) or (difference < 0 and is_ascending):
            return False
    
    return True