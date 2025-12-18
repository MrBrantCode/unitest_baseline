"""
QUESTION:
Create a function `is_unique_array` that determines if all elements in a given array are unique. The function must achieve a time complexity of O(n), where n represents the length of the array, and cannot use additional data structures beyond a set.
"""

def is_unique_array(arr):
    # Use a set to keep track of seen values
    seen = set()

    for num in arr:
        # If the value is already in the set, it is not unique
        if num in seen:
            return False
        
        # Add the value to the set
        seen.add(num)
    
    # If all values have been checked and no duplicates were found, return True
    return True