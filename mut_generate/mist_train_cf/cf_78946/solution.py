"""
QUESTION:
Design a function called `custom_contains` that takes three arrays as input: `array1`, `array2`, and `array3`. The function should return `True` if every element in `array2` is present at least once in `array1` and no element of `array3` is present in `array1`. The function should not use any built-in search or set operations and should have a time complexity of O(n), where n is the total number of elements in the three arrays.
"""

def entance(array1, array2, array3):
    # Step 1: Create a dictionary where keys are the elements of array1
    first_dict = {i:1 for i in array1}

    # Step 2: Check if all elements of array2 are in dictionary
    for ele in array2:
        if ele not in first_dict:
            return False

    # Step 3: Check if none of the elements of array3 are in dictionary
    for ele in array3:
        if ele in first_dict:
            return False

    # If both conditions are met, return True
    return True