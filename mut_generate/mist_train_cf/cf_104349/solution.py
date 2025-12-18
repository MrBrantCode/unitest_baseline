"""
QUESTION:
Find the second smallest number in a list of integers without using built-in sorting functions or libraries. The function should be named `find_second_smallest` and take a list of integers as input. The solution should have a time complexity of O(n) and use constant space. If the list has less than two distinct elements, the function should return the smallest element available.
"""

def find_second_smallest(lst):
    """
    Find the second smallest number in a list of integers without using built-in sorting functions or libraries.

    Args:
        lst (list): A list of integers.

    Returns:
        int: The second smallest number in the list. If the list has less than two distinct elements, returns the smallest element available.
    """
    smallest = float('inf')
    second_smallest = float('inf')
    for num in lst:
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif num < second_smallest and num != smallest:
            second_smallest = num
    if second_smallest == float('inf'):
        return smallest
    return second_smallest