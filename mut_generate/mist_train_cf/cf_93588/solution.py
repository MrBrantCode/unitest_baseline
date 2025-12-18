"""
QUESTION:
Implement a function called `find_second_maximum` that finds the second maximum element in a given array without using any built-in sorting functions or methods. The time complexity of the solution should be less than O(n^2).
"""

def find_second_maximum(arr):
    """
    Finds the second maximum element in a given array without using any built-in sorting functions or methods.

    Args:
        arr (list): A list of integers.

    Returns:
        int: The second maximum element in the array.
    """
    max1 = float('-inf')
    max2 = float('-inf')
    
    for num in arr:
        if num > max1:
            max2 = max1
            max1 = num
        elif num > max2 and num != max1:
            max2 = num
    
    return max2