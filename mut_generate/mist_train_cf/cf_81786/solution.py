"""
QUESTION:
Develop an algorithm to evaluate if the elements within a numeric array adhere to an ascending arithmetic progression. The function should handle arrays of varied sizes, from a minimum size of 3 elements up to a maximum of 10^6 elements. The function should return `True` if the array is an arithmetic progression and `False` otherwise. The input array can include both positive and negative integers as well as floating point numbers. The function should be named `is_arithmetic(array)`.
"""

def is_arithmetic(array):
    """Return True if array is an arithmetic progression."""
    
    # ensure the array has at least 3 elements
    if len(array) < 3:
        return False

    # compute the common difference between the first two elements
    diff = array[1] - array[0]

    # for each subsequent pair of elements
    for i in range(2, len(array)):
        # if the difference does not match the common difference, return False
        if array[i] - array[i - 1] != diff:
            return False

    # if we've made it here, the array is an arithmetic progression
    return True