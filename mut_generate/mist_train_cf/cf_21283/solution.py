"""
QUESTION:
Write a function `find_max_subarray_sum` that finds the maximum subarray sum of an array. The function should take one parameter `arr`, which can be an empty array or contain both positive and negative integers. The function should have a time complexity of O(n), where n is the length of the array, and should only traverse the array once. The solution should be implemented using dynamic programming and should not use any built-in functions or libraries.
"""

def find_max_subarray_sum(arr):
    """
    Finds the maximum subarray sum of an array.

    Args:
    arr (list): An array of integers.

    Returns:
    int: The maximum subarray sum.

    """
    if not arr:  
        return 0

    max_sum = arr[0]  
    current_sum = arr[0]  

    for i in range(1, len(arr)):
        current_sum = max(arr[i], current_sum + arr[i])  
        max_sum = max(max_sum, current_sum)  

    return max_sum