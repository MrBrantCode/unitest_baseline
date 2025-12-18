"""
QUESTION:
Develop a function named `second_smallest` that takes a list as an argument and returns the second smallest numerical value. The list may contain integers, floating point numbers, and strings. The function should exclude non-numerical values and return an error message if the list does not contain at least two numerical values.
"""

def second_smallest(lst):
    """
    Returns the second smallest numerical value in a list, 
    excluding non-numerical values. If the list does not 
    contain at least two numerical values, an error message 
    is returned.

    Args:
        lst (list): A list containing integers, floats, and strings.

    Returns:
        int or float: The second smallest numerical value in the list, 
                      or an error message if the list does not contain 
                      at least two numerical values.
    """
    nums = sorted(value for value in lst if isinstance(value, (int, float)))
    if len(nums) < 2:
        return 'The list does not contain at least two numerical values'
    return nums[1]