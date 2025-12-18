"""
QUESTION:
Create a function named `is_similarly_oriented` that takes an array of integers or floating point numbers as input. The function should return True if all non-zero elements in the array are similarly oriented (i.e., either all positive or all negative) and False otherwise. If the array is empty or contains only one element, or all elements are zero, the function should return True. The function should have a time complexity of O(n), where n is the length of the input array, and should handle large input arrays efficiently.
"""

def is_similarly_oriented(arr):
    if len(arr) < 2:
        return True
    
    is_positive = None
    
    for num in arr:
        if num > 0:
            if is_positive is None:
                is_positive = True
            elif not is_positive:
                return False
        elif num < 0:
            if is_positive is None:
                is_positive = False
            elif is_positive:
                return False
    
    return True