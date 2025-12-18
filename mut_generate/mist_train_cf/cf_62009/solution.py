"""
QUESTION:
Design a function called `binary_search` that uses a binary search algorithm to locate a specified integer `x` within a sorted list of integers (which can include negative and repeated values). The function should return the first and last position of `x` in the list and the count of its occurrences. If `x` is not found in the list, the function should return 'Element not found in array.' The function should achieve a time complexity of O(log n) and avoid unnecessary iterations.
"""

def binary_search(nums, x):
    """
    This function uses a binary search algorithm to locate a specified integer x within a sorted list of integers.
    
    Args:
    nums (list): A sorted list of integers.
    x (int): The target integer to be searched.

    Returns:
    tuple: A tuple containing the first and last position of x in the list and the count of its occurrences.
    If x is not found in the list, it returns 'Element not found in array.'
    """
    
    # Initialize the first and last position
    first_pos = -1
    last_pos = -1
    
    # Find the first occurrence of x
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] < x:
            left = mid + 1
        else:
            if nums[mid] == x:
                first_pos = mid
            right = mid - 1
    
    # If x is not found, return the message
    if first_pos == -1:
        return 'Element not found in array.'
    
    # Find the last occurrence of x
    left, right = first_pos, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] > x:
            right = mid - 1
        else:
            if nums[mid] == x:
                last_pos = mid
            left = mid + 1
    
    # Count the occurrences of x
    count = last_pos - first_pos + 1
    
    # Return the result
    return (first_pos, last_pos, count)