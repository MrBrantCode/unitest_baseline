"""
QUESTION:
Write a function named `largest_difference` that takes a list of integers as input and returns the largest difference between any two elements in the list. The function should achieve a time complexity of O(n) and use constant space. If the list contains less than 2 elements, the function should return 0.
"""

def largest_difference(lst):
    """
    This function calculates the largest difference between any two elements in a list.
    
    Args:
    lst (list): A list of integers.
    
    Returns:
    int: The largest difference between any two elements in the list. If the list contains less than 2 elements, it returns 0.
    """
    
    if len(lst) < 2:
        return 0
    
    min_num = lst[0]
    max_diff = lst[1] - min_num
    
    for i in range(2, len(lst)):
        if lst[i-1] < min_num:
            min_num = lst[i-1]
        diff = lst[i] - min_num
        if diff > max_diff:
            max_diff = diff
    
    return max_diff