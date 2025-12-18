"""
QUESTION:
Write a function `find_second_largest` that takes an array of integers as input and returns the second largest element. The function should run in O(n) time complexity and handle cases where the array is empty, contains only one element, or has duplicate elements. The function should not use built-in sorting or max functions. If there is no second largest element, the function should return "No second largest element".
"""

def find_second_largest(nums):
    """
    This function finds the second largest element in an array of integers.
    
    Args:
    nums (list): A list of integers.
    
    Returns:
    int or str: The second largest element if exists, otherwise "No second largest element".
    """
    
    if not nums:  # Check if the array is empty
        return "No second largest element"
    
    max_num = second_max = float('-inf')  # Initialize max and second max as negative infinity
    
    for num in nums:
        if num > max_num:  # If current number is greater than max, update max and second max
            second_max = max_num
            max_num = num
        elif num > second_max and num != max_num:  # If current number is greater than second max and not equal to max, update second max
            second_max = num
    
    if second_max == float('-inf'):  # If second max is still negative infinity, it means there is no second largest element
        return "No second largest element"
    
    return second_max