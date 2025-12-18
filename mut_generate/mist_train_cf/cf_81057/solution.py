"""
QUESTION:
Create a function called `check_element` that takes a list of numbers and a target number as inputs. The function should return the index of the target number in the list if found, and -1 if not found. The function should also validate that all elements in the list and the target number are either integers or floats, and return an error message if this condition is not met. The function should have a time complexity of O(n) or less.
"""

def check_element(arr, target):
    # Checks the data type of all elements of 'arr' 
    # If any is not int or float, an error message is returned
    for i in arr:
        if not isinstance(i, (int, float)):
            return "Error: All elements in the list must be either integers or floats"

    # Checks the data type of 'target', if it's not an int or a float, 
    # It returns an error message
    if not isinstance(target, (int, float)):
        return "Error: Target must be either integer or float"

    # Iterates over the list, returning the index of 'target' if found
    for i in range(len(arr)):
        if arr[i] == target:
            return i
            
    # If 'target' is not in 'arr', returns -1
    return -1