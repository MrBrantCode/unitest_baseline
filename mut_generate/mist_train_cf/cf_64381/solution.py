"""
QUESTION:
Write a function `prod_signs(arr)` that takes an array of unique non-zero integers as input and returns the compound product of the sign and values in the array. The function should return `None` if the input array is empty or contains zero. The array length can range from 1 to 100.
"""

def prod_signs(arr):
    if len(arr) == 0 or 0 in arr:
        return None
    
    arr = list(set(arr))  # Eliminate duplicates

    # Calculate products separately for positive and negative integers
    prod_positive = 1
    prod_negative = 1

    for x in arr:
        if x > 0:
            prod_positive *= x
        else:
            prod_negative *= x

    # Return result considering the signs
    return prod_positive * (prod_negative if prod_negative < 0 else 1)