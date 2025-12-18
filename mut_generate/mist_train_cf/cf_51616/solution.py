"""
QUESTION:
Write a recursive function `count_occurrences(arr, x)` that finds the number of occurrences of an element `x` in a list `arr` containing only integers. The function should return the total count of occurrences of `x` in `arr`.
"""

def entance(arr, x):
    # Base case: the list is empty
    if not arr:
        return 0
    else:
        # Recursively count the occurrences in the rest of the list
        rest_count = entance(arr[1:], x)
        
        # If the first element is the one we're looking for, increment the count
        if arr[0] == x:
            return 1 + rest_count
        else:
            return rest_count